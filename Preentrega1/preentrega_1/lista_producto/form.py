from django import forms

class Produtoformulario (forms.Form):
    name = forms.CharField(max_length=100)
    precio = forms.FloatField()
    stock = forms.BooleanField(required=False)