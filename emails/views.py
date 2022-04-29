from django.shortcuts import render, redirect
from .models import Persons
from django.http import HttpResponse
from .forms import usuarioForm

# Create your views here.


def home(request):
    usuarios = Persons.objects.all()
    if request.method == 'GET':
        form = usuarioForm()
    else:
        form = usuarioForm(request.POST)
        if form.is_valid():
            form.save()


    contexto = {
        "users":usuarios,
        "form": form
    }
    return render(request, 'emails/dashboard.html',contexto)


def editPerson(request, id):
    usuario = Persons.objects.get(id = id)
    if request.method == 'GET':
        form = usuarioForm(instance = usuario)
        contexto = {
            "form": form
        }
    else:
        form = usuarioForm(request.POST,instance=usuario)
        contexto = {
            "form": form
        }
        if form.is_valid():
            form.save()
            return redirect('/dashboard')

    return render(request, 'emails/editarUsuario.html', contexto)


def products(request):
    return render(request, "emails/editarUsuario.html")


def customer(request):
    return render(request, "emails/customer.html")
