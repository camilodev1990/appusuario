#appusuario/AppUsuario/urls.py

from django.urls import path
from apps_importadas.appusuario.AppUsuario import views

urlpatterns = [
    path('registro/', views.RegistroTemplateView.as_view(), name='registro'),
    path('login/', views.LoginTemplateView.as_view(), name=('login')),
]
