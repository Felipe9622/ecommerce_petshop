from django.db import models

STATUS = (
    ('doing', 'Doing'),
    ('done', 'Done'),
)

class Task(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    phone = models.CharField(max_length=11, verbose_name='Telefone', default=False)
    email = models.EmailField(blank=True, null=True,
                              verbose_name='E-mail', default=False)
    login = models.CharField(
        max_length=100, verbose_name='Login', default=False)
    password = models.CharField(
        max_length=100, verbose_name='Senha', default=False)
    done = models.CharField(
        max_length=15,
        choices=STATUS,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
