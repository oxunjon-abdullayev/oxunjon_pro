from django import forms

from app.models import ProductModel


class ProductForms(forms.ModelForm):

    class Meta:
        model = ProductModel

        exclude  =()

