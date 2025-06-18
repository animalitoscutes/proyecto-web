from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="inicio"),
   path('noticias/<uuid:pk>/', views.noticia, name="noticia"),
   path('form_post/', views.formulario, name='formulario'),
   path('delete_post/<str:pk>/',views.borrarpost, name="borrarpost"),
   path('registro/', views.registo, name='registro'),
   path('login/', views.login_page, name='login'),
   path('logout/', LogoutView.as_view(next_page='inicio'), name="logout"),
   path('editar-perfil/', views.editar_perfil, name='editar_perfil'),

   
    
]
