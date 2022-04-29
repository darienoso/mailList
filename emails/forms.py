from django import forms
from .models import Persons


class usuarioForm(forms.ModelForm):
    class Meta:
        model = Persons
        fields = '__all__'
