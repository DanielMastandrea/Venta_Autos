from multiprocessing import context
from django.shortcuts import render
from Productos.models import Autos


def create_car(request):
    autos = Autos.objects.all()
    context = {}
    nuevo_auto = Autos.objects.create(brand = 'Chevrolet', model = "Sonic", year = 2014, price = 20000000, stock = 1)
    context = {
            'nuevo_auto': nuevo_auto
        }
    return render(request, 'Productos/new_car.html', context=context)

def list_cars(request):
    autos = Autos.objects.all()
    print(len(autos))
    context = {
        'autos': autos
    }
    return render(request, 'Productos/car_list.html', context=context)