# Generated by Django 3.2.3 on 2021-12-09 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0026_auto_20211209_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='dadosProduct/'),
            preserve_default=False,
        ),
    ]
