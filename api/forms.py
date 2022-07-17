from django import forms
from django.forms import ModelForm

from .models import User, Excercise, Routine


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class ExcerciseForm(forms.ModelForm):
    class Meta:
        model = Excercise
        fields = '__all__'


class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['Routinename', 'RoutineExcercise']

        Routinename = forms.CharField()
        RoutineExcercise= forms.ModelMultipleChoiceField(
            queryset=Excercise.objects.all(),
            widget=forms.CheckboxSelectMultiple
        )

