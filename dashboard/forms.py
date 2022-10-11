from django import forms
from .models import Products


class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "product name"
    }))
    image= forms.CharField(widget=forms.TextInput(attrs={
        'type': "file",
        "class": "form-control",
        "placeholder": "image"
    }))
    
    amount = forms.CharField(widget=forms.TextInput(attrs={
        "type": "number",
        "class": "form-control",
        "placeholder": "amount"
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "Product description"
    }))
    class Meta:
        model = Products
        fields = [
            'name', 'image','amount','description'
        ]