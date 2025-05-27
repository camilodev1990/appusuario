#appusuario/AppUsuario/urls.py

from django.urls import path
from apps_importadas.appusuario.AppUsuario import views

urlpatterns = [
    path('registro/', views.RegistroTemplateView.as_view(), name='registro'),
    path('login/', views.LoginTemplateView.as_view(), name=('login')),
    path('logout/', views.LogoutTemplateView.as_view(), name='logout'),
    path('editar_usuario/', views.UsuarioUpdateTemplateView.as_view(), name='editar_usuario'),
]