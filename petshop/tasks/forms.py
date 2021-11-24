from django import forms

from .models import Task


class AddData(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('phone', 'email', 'name',
                  'animal_race', 'problem', 'appointment_date')
