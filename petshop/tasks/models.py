from django.db import models
from django.contrib.auth import get_user_model

STATUS = (
    ('pendente', 'Pendente'),
    ('finalizado', 'Finalizado'),
)

TYPE = (
    ('gato' , 'Gato'),
    ('cachorro' , 'Cachorro'),
    ('passaro' , 'Passaro'),
)


class Task(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Nome"
    )
    phone = models.CharField(
        max_length=11, 
        verbose_name='Telefone', 
        default=False
    )
    email = models.EmailField(
        blank=True, 
        null=True,
        verbose_name='E-mail', 
        default=False
    )

    animal_race = models.CharField(
    max_length=100,
    choices=TYPE,
    verbose_name='Tipo de animal',
    )

    problem = models.CharField(
        max_length=100, 
        verbose_name="sintoma do animal"
    )

    appointment_date = models.DateField('data', null=True, blank=True)

    done = models.CharField(
        max_length=15,
        choices=STATUS,
    )
    
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
