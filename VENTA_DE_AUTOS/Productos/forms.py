from io import BufferedRandom
from socket import fromshare
from django import forms

class Formulario_productos(forms.Form):
    brand = forms.CharField(max_length=100)
    model = forms.CharField(max_length=100)
    year = forms.IntegerField()
    price = forms.FloatField()
    description = forms.CharField(max_length=200)
    is_active = forms.BooleanField(default=True)
    creation_date = forms.DateField(auto_now_add=True, null=True, blank=True)
    stock = forms.IntegerField()
    