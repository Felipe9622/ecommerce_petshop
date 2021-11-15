from django.db import models

STATUS = (
    ('doing', 'Doing'),
    ('done', 'Done'),
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
    max_length=50,
    choices=TYPE,
    verbose_name='Tipo de animal',
    )

    problem = models.CharField(
        max_length=100, 
        verbose_name="sintoma do animal"
    )

    done = models.CharField(
        max_length=15,
        choices=STATUS,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
