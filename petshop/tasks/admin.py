from django.contrib import admin


from .models import Task
# para fazer a importação e extração precisa da biblioteca ImportExportModelAdmin
from import_export.admin import ImportExportModelAdmin
from tasks.models import Member, Task


#banco é novo então precisa registralo
@admin.register(Member)
class MemberAdmin(ImportExportModelAdmin):
    list_display = ("firstname", "lastname", "email", "birth_date")
    pass

#banco Task já estava cadastrado no app tasks então para que não de mensagem de erro precisa adicionar 
#como esta abaixo
@admin.register(Task)
class TaskAdmin(ImportExportModelAdmin):
    list_display = ("cpf", "phone", "email", "name",
                    "animal_race", "problem", "appointment_date", "hours", "done", "user",)
    pass
    admin.register(Task)

