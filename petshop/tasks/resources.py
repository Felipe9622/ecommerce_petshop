from import_export import resources
from tasks.models import Member, Task


class MemberResource(resources.ModelResource):
    class Meta:
        model = Member


class TaskResource(resources.ModelResource):
    class Meta:
        model = Task
