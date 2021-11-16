from django import forms

from .models import Task


class AddData(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'phone', 'email', 'animal_race', 'problem', 'user')
