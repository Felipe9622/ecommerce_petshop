from django.contrib import admin
from .models import Category, Brand, ProductAttribute, Size, Product
from import_export.admin import ImportExportModelAdmin
from ecommerce.models import Product

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


@admin.register(Product)
class Product1Admin(ImportExportModelAdmin):
    list_display = ("title", "image", "slug",
                    "detail", "specs", "category", "brand", "size", "status ",)
    pass
    admin.register(Product)



admin.site.register(ProductAdmin)


# Atributos do Produto
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag','product', 'price', 'size')
admin.site.register(ProductAttribute, ProductAttributeAdmin)


