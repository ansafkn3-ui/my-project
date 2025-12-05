from django import forms
from .models import Books,Event,Production

class Employee(forms.Form):
    name=forms.CharField(max_length=30)
    age=forms.IntegerField()

class Bookform(forms.ModelForm):
    class Meta:
        model=Books
        fields="__all__"

class Eventform(forms.ModelForm):
    class Meta:
        model=Event
        fields="__all__"


class Prodform(forms.ModelForm):
    class Meta:
        model=Production
        fields="__all__"