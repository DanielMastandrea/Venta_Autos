from django.shortcuts import render,redirect
from Productos.models import Autos 
from Productos.models import Ceros 
from Productos.models import Motos
from Productos.forms import Formulario_autos
from Productos.forms import Formulario_motos
from Productos.forms import Formulario_ceros

def create_car(request):
    if request.method == "POST":
        form = Formulario_autos(request.POST)
        if form.is_valid():
            Autos.objects.create(
                brand = form.cleaned_data['brand'],
                model = form.cleaned_data['model'],
                year = form.cleaned_data['year'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                is_active = form.cleaned_data['is_active'],
                stock = form.cleaned_data['stock']
            )
            return redirect(list_cars)
    elif request.method == 'GET':
        form = Formulario_autos()
    context = {'form':form}
    return render(request,'Productos/new_car.html', context = context)

def create_moto(request):
    if request.method == "POST":
        form = Formulario_motos(request.POST)
        if form.is_valid():
            Motos.objects.create(
                brand = form.cleaned_data['brand'],
                model = form.cleaned_data['model'],
                year = form.cleaned_data['year'],
                engine_cc = form.cleaned_data ["engine_cc"],
                horses_hp = form.cleaned_data ["horses_hp"],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                is_active = form.cleaned_data['is_active'],
                stock = form.cleaned_data['stock']
            )
            return redirect(list_cars)
    elif request.method == 'GET':
        form = Formulario_motos()
    context = {'form':form}
    return render(request,'Productos/new_car.html', context = context)

def create_cero(request):
    if request.method == "POST":
        form = Formulario_ceros(request.POST)
        if form.is_valid():
            Ceros.objects.create(
                brand = form.cleaned_data['brand'],
                model = form.cleaned_data['model'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                is_active = form.cleaned_data['is_active'],
                stock = form.cleaned_data['stock']
            )
            return redirect(list_ceros)
    elif request.method == 'GET':
        form = Formulario_ceros()
    context = {'form':form}
    return render(request,'Productos/new_car.html', context = context)



def list_cars(request):
    autos = Autos.objects.all()
    print(len(autos))
    context = {
        'autos': autos,
    }
    return render(request, 'Productos/car_list.html', context=context)

def list_motos(request):
    
    motos = Motos.objects.all()
    
    print(len(motos))
    context = {
        'motos': motos,
    }
    return render(request, 'Productos/motos_list.html', context=context)  

def list_ceros(request):
    ceros = Ceros.objects.all()
    print(len(ceros))
    context = {
        'ceros': ceros
    }
    return render(request, 'Productos/cero_list.html', context=context)


def search_products(request):
    search = request.GET['search']
    autos = Autos.objects.filter(brand__icontains=search)
    motos = Motos.objects.filter(brand__icontains=search)
    ceros = Ceros.objects.filter(brand__icontains=search)
    context = { 'autos': autos,
                'motos': motos,
                'ceros': ceros
    }
    return render(request, 'Productos/search_products.html', context=context)

