from django import forms

class Vendedorformulario (forms.Form):
    nombre = forms.CharField(max_length=100)
    nivel = forms.FloatField()
    activo = forms.BooleanField()