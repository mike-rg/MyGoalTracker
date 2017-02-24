from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import views
from django.http import JsonResponse

from usuario.models import Usuario
from usuario.forms import UserForm, UsuarioForm


def pagina_de_inicio(request):
    return render(request, 'inicio.html')


def registrar_usuario(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST, prefix="user")
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            perfil = Usuario()
            # "Usuario.usuario" debe ser una instancia de "User"
            perfil.usuario = user
            perfil.save()
            return redirect('/login/')
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
def modificar_perfil_usuario(request):
    user = request.user
    usuario = Usuario.objects.get(usuario=user.id)
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        usuario_form = UsuarioForm(request.POST, request.FILES, instance=usuario)
        if usuario_form.is_valid() and user_form.is_valid():
            user = user_form.save()
            usuario = usuario_form.save()
            user.save()
            usuario.save()
            return redirect('/principal/')
    else:
        user_form = UserForm()
        usuario_form = UsuarioForm() 

    context = {
        "user_form": user_form,
        "usuario_form": usuario_form,
    }
    return render(request, 'perfil.html', context)


@login_required
def perfil_usuario(request):
    user = request.user
    nombre_usuario = user.username
    usuario = Usuario.objects.get(usuario=user.id)
    foto_perfil = usuario.foto

    data = {
        'nombre_usuario': nombre_usuario,
        'foto_perfil_url' : foto_perfil.url,
    }
    return JsonResponse(data)
