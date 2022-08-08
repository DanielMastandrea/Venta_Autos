from django.urls import path
from Productos.views import list_cars, create_car, search_products


urlpatterns = [
    path('list-cars/', list_cars, name='list-cars'),
    path('create-car/', create_car, name='create-car'),
    path('search-products/', search_products, name ='search-products')
]