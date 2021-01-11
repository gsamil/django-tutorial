from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                "placeholder": "custom title"
            }
        )
    )
    email = forms.EmailField()
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

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    # if i want my title to contain certain str
    # def clean_<my_field_name>

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("This is not a valid title")
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")
        return email


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
