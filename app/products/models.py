#from django.db import models
#from ckeditor.fields import RichTextField

#class Product(models.Model):
#    name = models.CharField(max_length=255)
#    description = RichTextField(blank=True)  # <-- CKEditor
#    price = models.DecimalField(max_digits=10, decimal_places=2)
#    image = models.ImageField(upload_to='products/', blank=True, null=True)
#    created_at = models.DateTimeField(auto_now_add=True)
#    updated_at = models.DateTimeField(auto_now=True)

#    def __str__(self):
#        return self.name


from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=_("Nom du produit")
    )

    description = RichTextField(
        blank=True,
        verbose_name=_("Description du produit")
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Prix du produit")
    )

    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True,
        verbose_name=_("Image du produit")
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Date de création")
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Date de mise à jour")
    )

    class Meta:
        verbose_name = _("Produit")
        verbose_name_plural = _("Produits")

    def __str__(self):
        return self.name

