# Generated by Django 3.2.3 on 2021-12-02 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0017_alter_size_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='slug_padrao'),
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Preço'),
        ),
    ]
