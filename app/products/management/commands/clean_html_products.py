from django.core.management.base import BaseCommand
from app.products.models import Product
from app.products.serializers_mixins import CleanHTMLMixin


class Command(BaseCommand):
    help = "Nettoie le HTML des descriptions de produits existants dans la base de données"

    def handle(self, *args, **options):
        cleaner = CleanHTMLMixin()
        cleaned_count = 0
        total_products = Product.objects.count()

        self.stdout.write(self.style.NOTICE(f" Nettoyage du HTML pour {total_products} produits..."))

        for product in Product.objects.all():
            if product.description:
                old_desc = product.description
                new_desc = cleaner.clean_html(product.description)

                if old_desc != new_desc:
                    product.description = new_desc
                    product.save()
                    cleaned_count += 1
                    self.stdout.write(self.style.SUCCESS(f"Produit nettoyé : {product.name}"))

        self.stdout.write(self.style.SUCCESS(f"Nettoyage terminé ! {cleaned_count} produit(s) mis à jour."))
