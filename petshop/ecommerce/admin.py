from django.contrib import admin
from .models import Category, Brand, Size, Product


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Size)

class ProductAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'brand', 'size', 'status')
    list_editable=('status',)
admin.site.register(Product,ProductAdmin)

