from datetime import datetime

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.models import F, When
from django.shortcuts import render, redirect
from .models import Persons
from django.http import HttpResponse
from .forms import usuarioForm
from .filters import PersonFilter
from django.conf import settings
from django.core.mail import send_mail



# Create your views here.
@login_required
def home(request):
    usuarios = Persons.objects.all()
    myFilter = PersonFilter(request.GET, queryset=usuarios)
    usuarios = myFilter.qs
    # print(str(Sells.query))
    print(str(request.GET.get('Ciudad') != ""))

    if request.method == 'POST':
        sendEmail(request,usuarios)

    contexto = {
        "users": usuarios.values(),
        "myFilter": myFilter,
    }
    return render(request, 'emails/dashboard.html', contexto)


@login_required
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

@login_required
def editPerson(request, id):
    usuario = Persons.objects.get(Cedula=id)
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


@login_required
def deletePerson(request, id):
    usuario = Persons.objects.get(Cedula=id)
    usuario.delete()
    return redirect('/dashboard')

#
# def products(request):
#     form = productoForm()
#     contexto = {
#         "form": form,
#     }
#     if request.method == 'POST':
#         form = productoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/dashboard')
#
#     return render(request, "emails/crearProducto.html",contexto)


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


@login_required
def sendEmail(request,personas):


    print("Dentro de la funcion SendEmail")
    print("Linea 68: ", request.method)

    for user in personas:
        subject = f'{user.Nombre} - Necesitas ver esto! '
        message = f'{user.Ciudad},{datetime.now().date()} \n\n' \
                  f'Hola {user.Nombre}, \n\n' \
                  f'Cordial Saludo,\n'
        if request.GET.get('Ciudad') is not "":
            message += f"Aprovecha las promociones especiales que tenemos en {user.Ciudad}. \n"

        if request.GET.get('start_age') is not "" or request.GET.get('final_age') is not "":
            message += f"Encuentra todo lo que necesitas especialmente para ti, de regreso a la U \n"

        if request.GET.get('start_date_min') is not "" or request.GET.get('start_date_max') is not "":
            message += f"Te extranamos desde tu ultima Compra, te esperamos con nuevos productos. \n"
        message += f"Los mejores productos al mejor precio, lo encuentras en un solo lugar, visitanos\n!"
        message += f"Que tenga un feliz dia!\nAtentamente,\n\nLA CACHARRERIA UNIVERSAL S.A"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.Email]
        print("Sending Emails to: ",user.Email)
        # send_mail(subject, message, email_from, recipient_list)
        print(message)



def salir(request):
    logout(request)
    return redirect('/')
