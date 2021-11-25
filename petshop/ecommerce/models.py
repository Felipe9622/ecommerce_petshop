from django.db import models

#Categoria
class Category(models.Model):
    title = models.CharField(max_length=100,
    verbose_name='categoria do produto')

    image = models.ImageField(upload_to='categoria',
    verbose_name='imagem do produto')

    def __str__(self):
        return self.title

#Marca
class Brand(models.Model):
    title = models.CharField(max_length=100,
    verbose_name='marca do produto')

    image = models.ImageField(upload_to='marca',
    verbose_name='imagem do produto')

    def __str__(self):
        return self.title


#Tamanho 
class Size(models.Model):
    title = models.CharField(max_length=100,
    verbose_name='tamanho do produto')


    def __str__(self):
        return self.title


#Modelo do Produto
class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='produto')
    slug = models.CharField(max_length=400)
    detail = models.TextField()
    specs = models.TextField()
    price = models.PositiveIntegerField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
