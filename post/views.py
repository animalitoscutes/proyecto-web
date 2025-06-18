from django.shortcuts import render, get_object_or_404, redirect

from .models import post

from .forms import postform, Registroform, PerfilForm

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .models import Perfil
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
# Create your views here.


def home(request):
    posts=post.objects.all()
    context={'posts': posts}
    return render(request, "post/home.html", context)

def noticia(request, pk):
    post_obj = get_object_or_404(post, id=pk)
    context = {'post': post_obj}
    return render(request, "post/noticias.html", context)


@login_required
def formulario(request):
    form = postform()
    if request.method == 'POST':
        form = postform(request.POST, request.FILES)
        if form.is_valid():
            post_obj = form.save(commit=False)  # No guardar aún en BD
            post_obj.autor = request.user       # Asignar autor aquí
            post_obj.save()                     # Guardar en BD
            return redirect("inicio")
    context = {'form': form}
    return render(request, "post/agregar.html", context)

@login_required
def borrarpost(request, pk):
    post_obj = get_object_or_404(post, id=pk)

    # Verificar que el usuario logueado es el autor del post
    if post_obj.autor != request.user:
        return HttpResponseForbidden("No tienes permiso para borrar este post")

    if request.method == 'POST':
        post_obj.delete()
        return redirect("inicio")

    context = {'post_obj': post_obj}
    return render(request, "post/noticias.html", context)


def registo(request):
    formulario=Registroform()
    if request.method=='POST':
        formulario=Registroform(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    context={"formulario":formulario}

    return render(request, 'post/registro.html', context)

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'post/login.html', {"form": form})

@login_required
def editar_perfil(request):
    user = request.user
    posts_user = post.objects.filter(autor=user).order_by('-fecha_creacion')  

    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES, instance=user.perfil)
        if form.is_valid():
            form.save()
            
    else:
        form = PerfilForm(instance=user.perfil)

    context = {
        'form': form,
        'posts_user': posts_user,
    }
    return render(request, 'post/editar_perfil.html', context)