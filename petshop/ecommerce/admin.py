from django.contrib import admin
from .models import Category, Brand, ProductAttribute, Size, Product


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Size)

class ProductAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'brand', 'size', 'status')
    list_editable=('status')
admin.site.register(Product,ProductAdmin)

# Atributos do Produto


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'price', 'size' )
admin.site.register(ProductAttribute, ProductAttributeAdmin)
