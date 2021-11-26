from django.db import models


#Banner
class Banner(models.Model):
    img = models.CharField(max_length=200)
    alt_text = models.CharField(max_length=32)

#Categoria
class Category(models.Model):
    title = models.CharField(max_length=100,
    verbose_name='categoria do produto')

    image = models.ImageField(upload_to='ecommerce/cofre/dadosCategory',
    verbose_name='imagem do produto')

    def __str__(self):
        return self.title

#Marca
class Brand(models.Model):
    title = models.CharField(max_length=100,
    verbose_name='marca do produto')

    image = models.ImageField(upload_to='ecommerce/cofre/dadosBrand',
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
    title = models.CharField(max_length=200, verbose_name='titulo do produto')
    # upload_to ciria uma pasta e todas as fotos que
    image = models.ImageField(upload_to='ecommerce/cofre/dadosProduct')
    #forem adicionadas ficaram guardadas na pasta 
    slug = models.CharField(max_length=400)
    detail = models.TextField(verbose_name='detalhes')
    specs = models.TextField(verbose_name='especificações')

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    #models.BooleanField(default=True) apresenta a opção para flegar se esta valida ou não 

    def __str__(self):
        return self.title


# Atributos do Produto
class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.product.title
    
