from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.


class post(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    Noticia = models.TextField(null=True, blank=True)
    imagen_portada = models.ImageField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='perfiles/', default='perfiles/default.png')

    def __str__(self):
        return f'Perfil de {self.user.username}'
    

