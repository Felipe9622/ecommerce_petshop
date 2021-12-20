from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Task


@admin.register(Task)
class TaskAdmin(ImportExportModelAdmin):
    list_display = ("cpf", "phone", "email", "name", "animal_race",
                    "problem", "appointment_date", "hours", "done", "user",)
    pass
    admin.register(Task)

