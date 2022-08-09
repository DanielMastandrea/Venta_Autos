from django.urls import path
from Productos.views import list_cars,list_motos,list_ceros ,create_car, create_moto, create_cero ,search_products



urlpatterns = [
    path('list-cars/', list_cars, name='list-cars'),
    path('list-motos/', list_motos, name='list-motos'),
    path('list-ceros/', list_ceros, name='list-ceros'),
    path('create-car/', create_car, name='create-car'),
    path('create-moto/', create_moto, name='create-moto'),
    path('create-cero/', create_cero, name='create-cero'),
    path('search-products/', search_products, name ='search-products')
]