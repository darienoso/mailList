from django.db.models import F
from django.shortcuts import render, redirect
from .models import Persons, Productos
from django.http import HttpResponse
from .forms import usuarioForm, productoForm
from .filters import PersonFilter
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def home(request):
    # usuarios = Persons.objects.all()
    usuarios = Productos.objects.all()
    # usuarios = Productos.objects.select_related('spersonId')
    # usuarios = Productos.objects.filter(Persons=spersonsId)
    myFilter = PersonFilter(request.GET, queryset=usuarios)
    usuarios = myFilter.qs
    # print(str(Sells.query))
    print(str(usuarios.query))

    if request.method == 'POST':
        sendEmail(request,usuarios)

    contexto = {
        "users": usuarios.values(),
        "myFilter": myFilter,
        # "sells": Sells,
    }
    return render(request, 'emails/dashboard.html', contexto)

def crearPerson(request):
    form = usuarioForm()
    contexto = {
        "form": form,
    }
    if request.method == 'POST':
        form = usuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')

    return render(request, 'emails/crearUsuario.html', contexto)


def editPerson(request, id):
    usuario = Persons.objects.get(personId=id)
    usuario = Persons.objects.get(personId=id)
    if request.method == 'GET':
        form = usuarioForm(instance=usuario)
        contexto = {
            "form": form
        }
    else:
        form = usuarioForm(request.POST, instance=usuario)
        contexto = {
            "form": form
        }
        if form.is_valid():
            form.save()
            return redirect('/dashboard')

    return render(request, 'emails/editarUsuario.html', contexto)


def deletePerson(request, id):
    usuario = Persons.objects.get(personId=id)
    usuario.delete()
    return redirect('/dashboard')


def products(request):
    form = productoForm()
    contexto = {
        "form": form,
    }
    if request.method == 'POST':
        form = productoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')

    return render(request, "emails/crearProducto.html",contexto)


#
# def hacerVenta(request):
#     form = ventaForm()
#     contexto = {
#         "form": form,
#     }
#
#     if request.method == 'POST':
#         print("Datos del post: ", form)
#         form = ventaForm(request.POST)
#
#         if form.is_valid():
#             print("Guardando Datos")
#             form.save()
#             return redirect('/dashboard')
#
#     return render(request, "emails/hacerVenta.html",contexto)


def sendEmail(request,personas):
    print("Dentro de la funcion SendEmail")
    print("Linea 68: ", request.method)

    for user in personas:
        subject = 'Soy yo'
        message = f'Hi {user.pname}, Mensaje desde Django.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        print("Sending Emails to: ",user.email)
        # send_mail(subject, message, email_from, recipient_list)
        print("Enviado")


def login(request):
    return render(request, "emails/login.html")
