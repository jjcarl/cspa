from django import forms

from .models import Treatment, Product


class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        exclude = ['active']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'description': forms.TextInput(attrs={'class': 'form-control'}),
                   'price': forms.NumberInput(attrs={'class': 'form-control'})}


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['appointment', 'active']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'description': forms.TextInput(attrs={'class': 'form-control'})}
