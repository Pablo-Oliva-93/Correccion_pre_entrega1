from django import forms

class Usuarioformulario (forms.Form):
    usuario = forms.CharField(max_length=100)
    nombre = forms.CharField(max_length=100)
    edad = forms.FloatField()