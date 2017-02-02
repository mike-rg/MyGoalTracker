from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from usuario.models import Usuario


@login_required
def principal(request):
    user = request.user
    usuario = Usuario.objects.get(usuario=user.id)
    nombre_usuario = user.username
    foto_perfil_usuario = usuario.foto
    context = {
        "nombre_usuario" : nombre_usuario,
        "foto_perfil_usuario" : foto_perfil_usuario,
    }
    return render(request, 'principal.html', context)
