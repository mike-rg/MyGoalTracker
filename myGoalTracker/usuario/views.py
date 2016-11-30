from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import views

from usuario.models import Usuario


def pagina_de_inicio(request):
    return render(request, 'inicio.html')


def registrar_usuario(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST, prefix="user")
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            return redirect('/login')
    else:
        user_form = UserCreationForm(prefix="user")

    context = {
        "user_form": user_form,
    }
    return render(request, 'registrar.html', context)


def login_usuario(request):
    # La funcion login tiene mas parametros. Ver documentacion
    template_response = views.login(request, template_name='login.html')
    # Se puede modificar template_response antes de retornar.
    # Ver documentacion de TemplateResponse
    return template_response


@login_required
def logout_usuario(request):
    template_response = views.logout(request, template_name='inicio.html')
    return template_response


@login_required
def perfil_usuario(request):
    return render(request, 'perfil.html')
