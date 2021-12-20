from import_export import resources
from tasks.models import Task




class TaskResource(resources.ModelResource):
    class Meta:
        model = Task

