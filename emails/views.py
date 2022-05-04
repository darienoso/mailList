from django.shortcuts import render, redirect
from .models import Persons
from django.http import HttpResponse
from .forms import usuarioForm
from .filters import PersonFilter
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.


def home(request):
    usuarios = Persons.objects.all()
    myFilter = ""
    if request.method == 'GET':
        form = usuarioForm()
        myFilter = PersonFilter(request.GET,queryset=usuarios)
        usuarios = myFilter.qs
        sendEmail(usuario.name)
    else:
        form = usuarioForm(request.POST)
        if form.is_valid():
            form.save()


    contexto = {
        "users":usuarios,
        "form": form,
        "myFilter": myFilter,
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

def deletePerson(request,id):
    usuario = Persons.objects.get(id=id)
    usuario.delete()
    return redirect('/dashboard')



def products(request):
    return render(request, "emails/editarUsuario.html")


def customer(request):
    return render(request, "emails/eliminarUsuario.html")

def sendEmail(name):
    subject = 'welcome to GFG world'
    message = f'Hi {name}, thank you for registering in geeksforgeeks.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email, ]
    send_mail( subject, message, email_from, recipient_list )

