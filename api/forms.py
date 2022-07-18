from django import forms
from django.forms import ModelForm


from .models import User, Excercise, Routine


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class ExcerciseForm(ModelForm):
    class Meta:
        model = Excercise
        fields = '__all__'


class RoutineForm(ModelForm):
    class Meta:
        model = Routine
        fields = ['name', 'excercise']

        # Routinename = forms.CharField()
        # RoutineExcercise= forms.ModelMultipleChoiceField(
        #     queryset=Excercise.objects.all(),
        #     widget=forms.CheckboxSelectMultiple
        # )

