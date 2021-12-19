from django.contrib import admin
from .models import Task
from import_export.admin import ImportExportModelAdmin
from tasks.models import Member, Task


@admin.register(Member)
class MemberAdmin(ImportExportModelAdmin):
    list_display = ("firstname", "lastname", "email", "birth_date")
    pass


@admin.register(Task)
class TaskAdmin(ImportExportModelAdmin):
    list_display = ("cpf", "phone", "email", "name",
                    "animal_race", "problem", "appointment_date", "hours", "done", "user",)
    pass
    admin.register(Task)
