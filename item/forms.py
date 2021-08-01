from django import forms
from django.db.models.base import Model
from django.forms import ModelForm, widgets
from .models import Item
from crispy_forms.helper import FormHelper

#class ItemForm(forms.Form):
#    product_name = forms.CharField()
#    quantity = forms.IntegerField()
#    size = forms.ChoiceField(choices=[('S','Short'), ('M','Medium'),('L','Long')])
#    date = forms.DateField()


class DateInput(forms.DateInput):
   input_type = 'date'


class ItemForm(ModelForm):
    sold = forms.CharField(initial=0,
                           widget=forms.TextInput(attrs={
                               'id': 'sssd',
                               'class': 'sssd'
                           }),

                           )

    left = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'lllt',
            'class': 'lllt',
            'placeholder': 'Enter total number of items here also.',

        })
    )

    class Meta:
        model = Item
        widgets = {'date': DateInput()}
        fields = ['product_name', 'quantity', 'size', 'date', 'sold', 'left']
