from django.contrib import admin
from Productos.models import Autos

@admin.register(Autos)
class Autos_admin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'year', 'price', 'description', 'is_active', 'creation_date', 'stock']
