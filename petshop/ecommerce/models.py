from django.db import models


#Banner
class Banner(models.Model):
    img = models.CharField(max_length=200)
    alt_text = models.CharField(max_length=32)

    class Meta:  # substitui o nome no banco de dados na pagina do admin
        verbose_name_plural = 'Banner'

    def __str__(self):
        return self.alt_text


#Categoria
class Category(models.Model):
    title = models.CharField(max_length=100,
    verbose_name='categoria do produto')

    image = models.ImageField(upload_to="dadosCategory/",
    verbose_name='imagem do produto')

    class Meta:  # substitui o nome no banco de dados na pagina do admin
        verbose_name_plural = 'Categoria'

    def __str__(self):
        return self.title

#Marca
class Brand(models.Model):
    title = models.CharField(max_length=100,
    verbose_name='marca do produto')

    image = models.ImageField(upload_to='dadosBrand/',
    verbose_name='imagem do produto')

    class Meta:  # substitui o nome no banco de dados na pagina do admin
        verbose_name_plural = 'Marca'

    def __str__(self):
        return self.title


#Tamanho 
class Size(models.Model):
    title = models.CharField(max_length=100,
    verbose_name='tamanho do produto')

    class Meta:  # substitui o nome no banco de dados na pagina do admin
        verbose_name_plural = 'Tamanho'

    def __str__(self):
        return self.title


#Modelo do Produto
class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='titulo do produto')
    # upload_to ciria uma pasta e todas as fotos que
    image = models.ImageField(upload_to='dadosProduct/')
    #forem adicionadas ficaram guardadas na pasta 
    slug = models.CharField(max_length=400)
    detail = models.TextField(verbose_name='detalhes')
    specs = models.TextField(verbose_name='especificações')

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    #models.BooleanField(default=True) apresenta a opção para flegar se esta valida ou não 

    class Meta:  # substitui o nome no banco de dados na pagina do admin
        verbose_name_plural = 'Produto'

    def __str__(self):
        return self.title


# Atributos do Produto
class ProductAttribute(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='Produto')
    size = models.ForeignKey(
        Size, on_delete=models.CASCADE, verbose_name='Tamanho')
    price = models.PositiveIntegerField(verbose_name='Peso')

    class Meta:  # substitui o nome no banco de dados na pagina do admin
        verbose_name_plural = 'Atributos do Produto'

    def __str__(self):
        return self.product.title
    
