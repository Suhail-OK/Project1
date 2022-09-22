from django import forms
from django.forms import fields
from .models import *

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'

class FoodListForm(forms.ModelForm):
    class Meta:
        model = FoodList
        fields = '__all__'