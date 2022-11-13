from django.contrib import admin

from product.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','company', 'created_at', 'updated_at')
    list_filter = ( 'price','company', 'created_at', 'updated_at')
    search_fields = ('name','company__name','price','created_at', 'updated_at')
admin.site.register(Product, ProductAdmin)