from django.forms import ModelForm
from django import forms
from .models import post
from tinymce.widgets import TinyMCE
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil


class postform(ModelForm):
    Noticia = forms.CharField(widget=TinyMCE(attrs={
        'cols': 80,
        'rows': 30,
        'style': 'width: 100%; height: 400px;',
    }, mce_attrs={
        'menubar': True,
        'plugins': 'advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code fullscreen insertdatetime media table paste help wordcount',
        'toolbar': 'undo redo | formatselect | bold italic backcolor | \
                    alignleft aligncenter alignright alignjustify | \
                    bullist numlist outdent indent | removeformat | help',
        'height': 400,
        'branding': False,
    }))
    class Meta:
        model = post
        exclude = ['autor'] 

class Registroform(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto']