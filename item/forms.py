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
    quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'id': 'qqqt',
            'class': 'qqqt'
        })
    )

    sold = forms.CharField(initial=0,
                           widget=forms.TextInput(attrs={
                               'id': 'sssd',
                               'class': 'sssd',
                               'readonly':'readonly'
                               
                           })

                           )

    left = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'lllt',
            'class': 'lllt',
            'readonly':'readonly',
            'placeholder':'It will automatically get filled.'
        })
    )

    class Meta:
        model = Item
        widgets = {'date': DateInput()}
        fields = ['product_name', 'quantity', 'size', 'date', 'sold', 'left']
