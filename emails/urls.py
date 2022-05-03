from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.home),
    path('products/', views.products),
    path('customer/', views.customer),
    path('editarUsuario/<int:id>', views.editPerson),
    path('eliminarUsuario/<int:id>', views.deletePerson),

]
