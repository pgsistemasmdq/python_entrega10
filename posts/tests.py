from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse
from pathlib import Path
from tempfile import TemporaryDirectory
from .models import Post


class CrudTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.media_temporal = TemporaryDirectory()
        cls.media_override = override_settings(MEDIA_ROOT=cls.media_temporal.name)
        cls.media_override.enable()

    @classmethod
    def tearDownClass(cls):
        cls.media_override.disable()
        cls.media_temporal.cleanup()
        super().tearDownClass()

    def test_crear_editar_y_eliminar_post(self):
        respuesta = self.client.post(reverse("posts:crear_post"), {
            "titulo": "Nuevo post", "contenido": "Prueba", "autor": "Carlos", "estado": "publicado",
        })
        self.assertEqual(respuesta.status_code, 302)
        post = Post.objects.get(titulo="Nuevo post")
        self.assertEqual(self.client.get(reverse("posts:detalle_post", args=[post.pk])).status_code, 200)
        self.client.post(reverse("posts:editar_post", args=[post.pk]), {
            "titulo": "Editado", "contenido": "Prueba", "autor": "Carlos", "estado": "publicado",
        })
        post.refresh_from_db()
        self.assertEqual(post.titulo, "Editado")
        self.assertEqual(self.client.get(reverse("posts:eliminar_post", args=[post.pk])).status_code, 200)
        self.client.post(reverse("posts:eliminar_post", args=[post.pk]))
        self.assertFalse(Post.objects.filter(pk=post.pk).exists())

    def test_formulario_acepta_imagen_valida(self):
        # Imagen PNG mínima (1x1) creada por Pillow.
        from io import BytesIO
        from PIL import Image
        buffer = BytesIO()
        Image.new("RGB", (1, 1), "white").save(buffer, format="PNG")
        archivo = SimpleUploadedFile("foto.png", buffer.getvalue(), content_type="image/png")
        respuesta = self.client.post(reverse("posts:crear_post"), {
            "titulo": "Con imagen", "contenido": "Contenido", "autor": "Carlos",
            "estado": "publicado", "imagen": archivo,
        })
        self.assertEqual(respuesta.status_code, 302)
        post = Post.objects.get(titulo="Con imagen")
        self.assertTrue(post.imagen.name.startswith("posts/"))
        self.assertTrue((Path(self.media_temporal.name)/post.imagen.name).exists())
