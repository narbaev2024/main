from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name_product', 'description', 'category', 'price', 'active', 'phone_number', 'image']
