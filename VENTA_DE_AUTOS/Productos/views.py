from django.shortcuts import render
from Productos.models import Autos
#from Productos.forms import Formulario_productos


def create_car(request):
    autos = Autos.objects.all()
    context = {}
    nuevo_auto = Autos.objects.create(brand = 'Chevrolet', model = "Prisma", year = 2019, price = 36000000, stock = 1)
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

def search_products(request):
    search = request.GET['search']
    products = Autos.objects.filter(name__icontains=search)
    context = {'products':products}
    return render(request, 'Productos/search_products.html', context=context)