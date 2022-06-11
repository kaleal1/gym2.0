from django import forms
from .models import User, Excercise


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class ExcerciseForm(forms.ModelForm):
    class Meta:
        model = Excercise
        fields = '__all__'
