# Generated by Django 3.2.3 on 2021-11-28 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0011_auto_20211127_0210'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name_plural': 'Marca'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categoria'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Produto'},
        ),
        migrations.AlterModelOptions(
            name='productattribute',
            options={'verbose_name_plural': 'Atributos do Produto'},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'verbose_name_plural': 'Tamanho'},
        ),
    ]
