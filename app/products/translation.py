#from modeltranslation.translator import TranslationOptions, translator
#from .models import Product

#class ProductTranslationOptions(TranslationOptions):
#    fields = ('description',)

#translator.register(Product, ProductTranslationOptions)
from modeltranslation.translator import register, TranslationOptions
from .models import Product

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('description',)
