from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.home, name='home'),
    # path('crearProducto', views.products),
    # path('hacerVenta', views.hacerVenta),
    path('crearUsuario', views.crearPerson),
    path('editarUsuario/<int:id>', views.editPerson),
    path('eliminarUsuario/<int:id>', views.deletePerson),
    path('salir/', views.salir, name="salir"),


]
