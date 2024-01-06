from django import forms
from django.forms import ModelForm

class CartAmountForm(forms.Form):
    amount_box = forms.IntegerField()