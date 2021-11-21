# Generated by Django 3.2.3 on 2021-11-21 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20211121_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='animal_race',
            field=models.CharField(choices=[('gato', 'Gato'), ('cachorro', 'Cachorro'), ('passaro', 'Passaro'), ('hamster', 'Hamster'), ('peixe', 'Peixe'), ('coelho', 'Coelho'), ('porquinho_da_índia', 'Porquinho da índia')], max_length=100, verbose_name='Tipo de animal'),
        ),
    ]
