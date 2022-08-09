from django.contrib import admin
from Productos.models import Autos
from Productos.models import Motos
from Productos.models import Ceros


@admin.register(Autos)
class Autos_admin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'year', 'price', 'description', 'is_active', 'creation_date', 'stock']

@admin.register(Motos)
class Motos_admin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'year', "engine_cc", "horses_hp",'price', 'description', 'is_active', 'creation_date', 'stock']

@admin.register(Ceros)
class Ceros_admin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'price', 'description', 'is_active', 'creation_date', 'stock']        
