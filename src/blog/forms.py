from django import forms
from .models import Article


class ProductForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                "placeholder": "custom title"
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "new text field class name",
                "id": "new text field id",
                "placeholder": "custom placeholder",
                "rows": 20,
                "cols": 100
            })
    )
    active = forms.BooleanField()

    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active'
        ]