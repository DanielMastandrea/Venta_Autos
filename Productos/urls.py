from django.urls import path
from Productos.views import list_cars, create_car, search_products,login_request,register
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('list-cars/', list_cars, name='list-cars'),
    path('create-car/', create_car, name='create-car'),
    path('search-products/', search_products, name ='search-products'),
    path('Login/', login_request , name='Login'),
    path('Register/', register , name='Register'),
    path('logout/', LogoutView.as_view (template_name="Productos/logout.html"), name = "Logout")
]