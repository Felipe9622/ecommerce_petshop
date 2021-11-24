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

TIME = (
    ('9:00', '9:00'),
    ('10:00', '10:00'),
    ('11:00', '11:00'),
    ('12:00', '12:00'),
    ('13:00', '13:00'),
    ('14:00', '14:00'),
    ('15:00', '15:00'),
    ('16:00', '16:00'),
    ('17:00', '17:00'),
    ('18:00', '18:00'),
    ('19:00', '19:00'),
    ('20:00', '20:00'),
)

class Task(models.Model):
    cpf = models.CharField(
        max_length=11,
        verbose_name='digite seu cpf',

    )
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

    hours = models.CharField(
        max_length=5,
        verbose_name="horario do agendamento",
        choices=TIME,
    )

    done = models.CharField(
        verbose_name="Status",
        max_length=15,
        choices=STATUS,
    )
    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="Usuario",)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
