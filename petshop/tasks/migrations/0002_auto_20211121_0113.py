# Generated by Django 3.2.3 on 2021-11-21 01:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='login',
        ),
        migrations.RemoveField(
            model_name='task',
            name='password',
        ),
        migrations.AddField(
            model_name='task',
            name='animal_race',
            field=models.CharField(choices=[('gato', 'Gato'), ('cachorro', 'Cachorro'), ('passaro', 'Passaro')], default=1, max_length=100, verbose_name='Tipo de animal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='appointment_date',
            field=models.DateField(blank=True, null=True, verbose_name='data'),
        ),
        migrations.AddField(
            model_name='task',
            name='problem',
            field=models.CharField(default=1, max_length=100, verbose_name='sintoma do animal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='done',
            field=models.CharField(choices=[('pendente', 'Pendente'), ('finalizado', 'Finalizado')], max_length=15),
        ),
        migrations.AlterField(
            model_name='task',
            name='email',
            field=models.EmailField(blank=True, default=False, max_length=254, null=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='task',
            name='phone',
            field=models.CharField(default=False, max_length=11, verbose_name='Telefone'),
        ),
    ]
