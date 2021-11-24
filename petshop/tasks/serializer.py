from rest_framework import serializers
from tasks.models import Task

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'phone', 'email', 'name',
                  'animal_race', 'problem', 'appointment_date', 'done', 'user']
