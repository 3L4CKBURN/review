from django.contrib import admin

# Register your models here.

from .models import Product,Offer

class ProductAdmin(admin.ModelAdmin):
    list_display = ('company', 'model','price')
    list_filter=('company','model','price')
    search_fields=('company','price','model')

class OfferAdmin(admin.ModelAdmin):
    list_display=("code","discount")


    

admin.site.register(Product,ProductAdmin)
admin.site.register(Offer,OfferAdmin)
