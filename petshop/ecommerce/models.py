from django.db import models
from django.utils.html import mark_safe




#Categoria
class Category(models.Model):
    title = models.CharField(max_length=100,
    verbose_name='categoria do produto')

    image = models.ImageField(upload_to="dadosCategory/",
    verbose_name='imagem do produto')

    class Meta:  # verbose_name_plural substitui o nome no banco de dados na pagina do admin
        verbose_name_plural = '1.Categorias'

    def __str__(self):
        return self.title


#Marca
class Brand(models.Model):
    title = models.CharField(max_length=100,
    verbose_name='marca do produto')

    image = models.ImageField(upload_to='dadosBrand/',
    verbose_name='imagem do produto')

    class Meta:  # verbose_name_plural substitui o nome no banco de dados na pagina do admin
        verbose_name_plural = '3.Marcas'

    def __str__(self):
        return self.title


#Tamanho 
class Size(models.Model):
    title = models.CharField(max_length=100,
    verbose_name='tamanho do produto')

    class Meta:  # verbose_name_plural substitui o nome no banco de dados na pagina do admin
        verbose_name_plural = '4.Peso'

    def __str__(self):
        return self.title


#Modelo do Produto
class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='titulo do produto')
    #forem adicionadas ficaram guardadas na pasta 
    # upload_to ciria uma pasta e todas as fotos que
    image = models.ImageField(upload_to='dadosProduct/')
    slug = models.CharField(max_length=400)
    detail = models.TextField(verbose_name='detalhes')
    specs = models.TextField(verbose_name='especificações')
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    #models.BooleanField(default=True) apresenta a opção para flegar se esta valida ou não
    status = models.BooleanField(default=True)
    #is_featured vai ser habilitado para mostrar os produtos em destaque na pagina inicial
    is_featured = models.BooleanField(
        default=False, verbose_name='visivel na pagina principal')
    class Meta:  # verbose_name_plural substitui o nome no banco de dados na pagina do admin
        verbose_name_plural = '2.Produtos'
    


    def __str__(self):
        return self.title





# Atributos do Produto
class ProductAttribute(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='Produto')
    size = models.ForeignKey(
        Size, on_delete=models.CASCADE, verbose_name='Tamanho')
    price = models.CharField(max_length=100, verbose_name='Preço')
    # upload_to ciria uma pasta e todas as fotos que
    image = models.ImageField(upload_to='dadosProduct/')

    class Meta:  # verbose_name_plural substitui o nome no banco de dados na pagina do admin
        verbose_name_plural = '5.Atributos do Produto'

    def __str__(self):
        return self.product.title
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" height="80"/>' % (self.image.url))
