

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0022_auto_20211202_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattribute',
            name='price',
            field=models.CharField(max_length=100, verbose_name='Preço'),
        ),
    ]
