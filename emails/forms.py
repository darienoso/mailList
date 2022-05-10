from django import forms
from .models import Persons, Productos


class usuarioForm(forms.ModelForm):
    class Meta:
        model = Persons
        fields = '__all__'


class productoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'
