from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


class RawProductForm(forms.Form):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                "placeholder": "custom title"
            }
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "new text field class name",
                "id": "new text field id",
                "placeholder": "custom placeholder",
                "rows": 20,
                "cols": 100
            })
    )
    price = forms.DecimalField()
