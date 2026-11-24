from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """Formulario para crear y editar publicaciones, con imagen opcional."""

    class Meta:
        model = Post
        fields = ("titulo", "contenido", "autor", "estado", "imagen")
        widgets = {
            "contenido": forms.Textarea(attrs={"rows": 7}),
        }
