from import_export import resources
from .models import Task

class TaskResources(resources.ModelResource):
    class Meta:
        model = Task