from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods
from .forms import PostForm
from .models import Post


def inicio(request):
    ultimos_posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")[:3]
    return render(request, "posts/inicio.html", {"ultimos_posts": ultimos_posts})


def acerca(request):
    return render(request, "posts/acerca.html")


def lista_posts(request):
    # Se listan todos los estados para poder gestionar también borradores.
    posts = Post.objects.all().order_by("-fecha_creacion")
    return render(request, "posts/lista_posts.html", {"posts": posts})


def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "posts/detalle_post.html", {"post": post})


@require_http_methods(["GET", "POST"])
def crear_post(request):
    formulario = PostForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and formulario.is_valid():
        post = formulario.save()
        messages.success(request, "Publicación creada correctamente.")
        return redirect("posts:detalle_post", pk=post.pk)
    return render(request, "posts/post_form.html", {"formulario": formulario, "accion": "Crear"})


@require_http_methods(["GET", "POST"])
def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    formulario = PostForm(request.POST or None, request.FILES or None, instance=post)
    if request.method == "POST" and formulario.is_valid():
        formulario.save()
        messages.success(request, "Publicación actualizada correctamente.")
        return redirect("posts:detalle_post", pk=post.pk)
    return render(request, "posts/post_form.html", {"formulario": formulario, "accion": "Editar"})


@require_http_methods(["GET", "POST"])
def eliminar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        messages.success(request, "Publicación eliminada.")
        return redirect("posts:lista_posts")
    return render(request, "posts/post_confirm_delete.html", {"post": post})
