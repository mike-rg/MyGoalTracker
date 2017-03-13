from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from usuario.models import Usuario
from meta.models import Meta
from meta.forms import MetaForm

from datetime import datetime


@login_required
def principal(request):
    return render(request, 'principal.html')


@login_required
def crear_meta(request):
    if request.method == "POST":
        usuario = Usuario.objects.get(usuario=request.user.id)
        meta_form = MetaForm(request.POST)
        if meta_form.is_valid():
            meta = meta_form.save()
            meta.usuario = usuario
            meta.save()
            return redirect('/principal/')
    else:
        meta_form = MetaForm()

    context = {
        "meta_form": meta_form,
    }
    return render(request, 'crear_meta.html', context)


@login_required
def editar_meta(request, pk):
    meta = Meta.objects.get(pk=pk)
    if request.method == "POST":
        meta_form = MetaForm(request.POST, instance=meta)
        if meta_form.is_valid():
            meta = meta_form.save()
            meta.save()
            return redirect('listar_metas')
    else:
        meta_form = MetaForm(instance=meta)

    context = {
        "meta_form": meta_form,
    }
    return render(request, 'crear_meta.html', context)


@login_required
def eliminar_meta(request, pk):
    meta = Meta.objects.get(pk=pk)
    meta.delete()
    return redirect('listar_metas')


@login_required
def listar_metas(request):
    usuario = Usuario.objects.get(usuario=request.user.id)
    metas = Meta.objects.filter(usuario=usuario)
    context = {
        "lista_metas": metas,
    }
    return render(request, 'listar_metas.html', context)