# Generated by Django 3.2.3 on 2021-11-21 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_task_appointment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='problem',
            field=models.TextField(max_length=100, verbose_name='sintoma do animal'),
        ),
    ]
