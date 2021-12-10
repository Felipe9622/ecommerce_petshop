from django.contrib import admin
from .models import Category, Brand, ProductAttribute, Size, Product


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Size)


#Modelo do Produto
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id',  'brand', 'size','status', 'is_featured', '__str__')
    class meta:
        model = Product
    # precisa manter a , logo apos que colocar 'status' se tirar vai apresentar uma mensagem de erro
    list_editable = ('status', 'is_featured')

admin.site.register(Product,ProductAdmin)

# Atributos do Produto
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag','product', 'price', 'size')
admin.site.register(ProductAttribute, ProductAttributeAdmin)
