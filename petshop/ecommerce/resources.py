from import_export import resources
from ecommerce.models import Product


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
