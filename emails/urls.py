from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home),
    path('products/', views.products),
    path('customer/', views.customer),
    path('editarUsuario/<int:id>', views.editPerson),
    path('eliminarUsuario/<int:id>', views.deletePerson),
    path('salir/', views.salir, name="salir")


]
