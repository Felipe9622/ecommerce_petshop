from rest_framework import serializers
from tasks.models import Task

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'phone', 'email', 'animal_race']
