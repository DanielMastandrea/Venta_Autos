from django.shortcuts import render,redirect
from Productos.models import Autos
from Productos.forms import Formulario_autos
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,authenticate

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

def list_cars(request):
    autos = Autos.objects.all()
    print(len(autos))
    context = {
        'autos': autos
    }
    return render(request, 'Productos/car_list.html', context=context)

def search_products(request):
    search = request.GET['search']
    autos = Autos.objects.filter(brand__icontains=search)
    context = {'autos': autos}
    return render(request, 'Productos/search_products.html', context=context)

def login_request (request):
    if request.method == "POST":
        form = AuthenticationForm (request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get ('username') 
            contra = form.cleaned_data.get ('password') 

            user = authenticate(username=usuario,password=contra)

            if user is not None:
                login (request,user)
                return render (request,"base.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render (request,"base.html", {"mensaje":"Error, datos incorrectos"})

        else:
                return render (request,"base.html", {"mensaje":"Error, formulario incorrecto"})

    form = AuthenticationForm

    return render (request,"Productos/login.html", {"form":form} )


def register (request):
    if request.method == "POST":
        form = UserCreationForm (request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get ('username') 
            form.save ()
            return render (request,"base.html", {"mensaje": "Usuario Creado"})
            
    else:
        form = UserCreationForm

    return render (request,"Productos/registro.html", {"form":form} )

    
    