from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.home),
    path('crearProducto', views.products),
    # path('hacerVenta', views.hacerVenta),
    path('crearUsuario', views.crearPerson),
    path('editarUsuario/<int:id>', views.editPerson),
    path('eliminarUsuario/<int:id>', views.deletePerson),
    path('', views.login),


]
