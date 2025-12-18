from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import strip_tags
from unfold.admin import ModelAdmin 
from django.utils.translation import gettext_lazy as _, get_language
from decimal import Decimal

from modeltranslation.admin import TabbedTranslationAdmin
from .models import Product
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field
import logging
from django.utils.html import strip_tags
from html import unescape

from . import translation


logger = logging.getLogger("app.products")


#class ProductResource(resources.ModelResource):
#    description_de = Field(attribute='description_de', column_name='description_de')
#    description_en = Field(attribute='description_en', column_name='description_en')
#    description_fr = Field(attribute='description_fr', column_name='description_fr')
    
#    class Meta:
#        model = Product
#        fields = (
#            'name',
#            'description_de',
#            'description_en',
#            'description_fr',
#            'price',
#            'image',
#        )
#        import_id_fields = ['name']
#        export_order = fields
#        skip_unchanged = True
#        report_skipped = False

#    #  Filtrer les produits AVANT export
#    def get_queryset(self):
#        return Product.objects.filter(
#            price__gt=0,
#            image__isnull=False,
#        ).exclude(
#            name__isnull=True
#        ).exclude(
#            name=""
#        )

#    #  Nettoyage texte (HTML + entités)
#    def clean_text(self, value):
#        if not value:
#            return ""
#        value = unescape(value)           # &eacute; → é
#        value = strip_tags(value)         # supprime HTML
#        return " ".join(value.split())    # supprime \n, &nbsp;, espaces multiples

#    def dehydrate_description_de(self, obj):
#        return self.clean_text(obj.description_de)

#    def dehydrate_description_en(self, obj):
#        return self.clean_text(obj.description_en)

#    def dehydrate_description_fr(self, obj):
#        return self.clean_text(obj.description_fr)

#    def dehydrate_image(self, obj):
#        return obj.image.name if obj.image else ""
        
class BaseProductAdmin(
    #ImportExportModelAdmin,
    ModelAdmin,  
    TabbedTranslationAdmin,
):
    translation_fallback_language = 'en'
    pass

@admin.register(Product)
class ProductAdmin(BaseProductAdmin):
    #sresource_class = ProductResource
    
    list_display = ( 'name', 'short_description', 'price', 'image_preview', 'created_at')
    list_display_links = ('name',)
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'description')  
    ordering = ('-created_at',)
    list_per_page = 4

    fieldsets = (
        (_('Main information'), {
            'fields': ('name', 'description', 'price'),  
        }),
        (_('Product image'), {
            'fields': ('image',),
        }),
        (_('Dates'), {
            'fields': ('created_at', 'updated_at'),
        }),
    )

    readonly_fields = ('created_at', 'updated_at', 'image_preview')

    actions = ['make_discount', 'set_price_to_zero']

    # Action 1 : réduction de 10%
    def make_discount(self, request, queryset):
        updated = 0
        # Log au début (optionnel)
        logger.info(f"Début de l'action réduction 10% par {request.user} – {queryset.count()} produits sélectionnés")

        for product in queryset:
            old_price = product.price
            product.price = (product.price * Decimal('0.9')).quantize(Decimal('0.01'))
            product.save(update_fields=["price", "updated_at"])

            logger.debug("Produit %s : %s € → %s €", product.id, old_price, product.price)
            updated += 1

        # Log final avec le bon nombre (et sans bug %
        logger.info(f"Réduction 10% appliquée sur {updated} produit(s) par {request.user}")

        if updated > 10:
            logger.warning("Volume important : %d produits modifiés par %s", updated, request.user)

        self.message_user(request, _(f"Réduction de 10 % appliquée sur {updated} produit(s)."))
    make_discount.short_description = _("Appliquer une réduction de 10%%")

    # Action 2 : mettre prix à zéro
    def set_price_to_zero(self, request, queryset):
        queryset.update(price=0)
        count = queryset.count()
        logger.critical("ACTION CRITIQUE → %s a mis %d produit(s) à 0 € !", request.user, count)
        self.message_user(request, _("Les prix ont été mis à 0."))
    set_price_to_zero.short_description = _("Mettre les prix à zéro")
    
    
    # Pour les sauvegardes via le formulaire (création / modification classique)
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if change:
            logger.info("Produit  ID %s est modifié par %s", obj.id, request.user)
        else:
            logger.info("Nouveau produit ID %s est créé  par %s", obj.id, request.user)

    # Bonus : loguer les suppressions
    def delete_queryset(self, request, queryset):
        count = queryset.count()
        
        # Log détaillé pour chaque produit
        for obj in queryset:
            logger.error("PRODUIT SUPPRIMÉ → ID %s | %s | par %s", obj.id, obj.name, request.user)
        
        # Log critique pour l’action globale
        logger.critical("SUPPRESSION MASSIVE → %d produit(s) supprimé(s) par %s", count, request.user)
        
        # On laisse Django faire le boulot
        super().delete_queryset(request, queryset)

    # Aperçu image
    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="60" style="border-radius: 8px;" />')
        return mark_safe('<span style="color: #888;">—</span>')
    image_preview.short_description = _("Aperçu")

    # Description courte selon langue active
    def short_description(self, obj):
        lang = get_language()  # récupère la langue active
        # essaie de prendre le champ traduit correspondant
        description_field = f'description_{lang}'
        if hasattr(obj, description_field):
            desc = getattr(obj, description_field)
            if desc:
                return strip_tags(desc)
        # fallback sur le champ principal
        return strip_tags(obj.description)
    short_description.short_description = _("Description")
