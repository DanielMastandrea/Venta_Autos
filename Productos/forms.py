from io import BufferedRandom
from django import forms

class Formulario_autos(forms.Form):
    brand = forms.CharField(max_length=100)
    model = forms.CharField(max_length=100)
    year = forms.IntegerField()
    price = forms.FloatField()
    description = forms.CharField(max_length=200)
    is_active = forms.BooleanField(initial=True)
    stock = forms.IntegerField()
    
class Formulario_motos(forms.Form):
    brand = forms.CharField(max_length=100)
    model = forms.CharField(max_length=100)
    year = forms.IntegerField()
    engine_cc = forms.IntegerField()
    horses_hp = forms.IntegerField()
    price = forms.FloatField()
    description = forms.CharField(max_length=200)
    is_active = forms.BooleanField(initial=True)
    stock = forms.IntegerField()
        
class Formulario_ceros(forms.Form):
    brand = forms.CharField(max_length=100)
    model = forms.CharField(max_length=100)
    price = forms.FloatField()
    description = forms.CharField(max_length=200)
    is_active = forms.BooleanField(initial=True)
    stock = forms.IntegerField()
            