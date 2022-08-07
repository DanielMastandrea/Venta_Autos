from django.shortcuts import render,redirect
from Productos.models import Autos
from Productos import *
#from  import Formulario_autos

def primer_formulario(request):
    print (request.method)
    if request.method == 'POST':
        Autos.objects.create(name = request.POST ['name'])
        return render(request, 'Productos/first_form.html', context = {})

def create_car(request):
    if request.method == "POST":
        form = Formulario_autos(request.POST)
        if form.is_valid():
            Autos.objects.create(
                brand = form.cleaned_data['name'],
                model = form.cleaned_data['model'],
                year = form.cleaned_data['year'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                is_active = form.cleaned_data['is_active'],
                creation_date = form.cleaned_data['creation_date'],
                stock = form.cleaned_data['stock']
            )
            return redirect(list_cars)
    #autos = Autos.objects.all()
    #context = {}
    #nuevo_auto = Autos.objects.create(brand = 'Chevrolet', model = "Prisma", year = 2019, price = 36000000, stock = 1)
    #context = {
            #'nuevo_auto': nuevo_auto
        #}
    #return render(request, 'Productos/new_car.html', context=context)

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