# Generated by Django 3.2.3 on 2021-11-25 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_auto_20211124_1852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='cars')),
            ],
        ),
    ]