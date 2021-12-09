# Generated by Django 3.2.3 on 2021-12-08 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0023_alter_productattribute_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productattribute',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(default=15, max_length=100, verbose_name='Preço'),
            preserve_default=False,
        ),
    ]
