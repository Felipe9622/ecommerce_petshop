from django.db import models
from datetime import datetime, date
from django.contrib.auth import get_user_model

STATUS = (
    ('pendente', 'Pendente'),
    ('finalizado', 'Finalizado'),
)

TYPE = (
    ('gato' , 'Gato'),
    ('cachorro' , 'Cachorro'),
    ('passaro' , 'Passaro'),
    ('hamster', 'Hamster'),
    ('peixe', 'Peixe'),
    ('coelho', 'Coelho'),
    ('porquinho_da_índia', 'Porquinho da índia'),
)


class Task(models.Model):
    phone = models.CharField(
        max_length=11, 
        verbose_name='Telefone', 

    )
    email = models.EmailField(
        blank=True, 
        null=True,
        verbose_name='E-mail', 

    )
    name = models.CharField(
        max_length=100,
        verbose_name="Nome do animal"
    )
    animal_race = models.CharField(
    max_length=100,
    choices=TYPE,
    verbose_name='Tipo de animal',
    )

    problem = models.TextField(
        max_length=100, 
        verbose_name="sintoma do animal"
    )

    appointment_date = models.DateField(
        verbose_name="data de agendamento (mm/dd/2021)",

        

    )

    done = models.CharField(
        max_length=15,
        choices=STATUS,
    )
    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
