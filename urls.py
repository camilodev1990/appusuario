#apps_importadas/appusuario/urls.py

from django.urls import path
from apps_importadas.appusuario import views

urlpatterns = [
    path('registro/', views.RegistroUsuarioView.as_view(), name='registro'),
    path('login/', views.CustomLoginView.as_view(), name=('login')),
    path('logout/', views.ConfirmLogoutView.as_view(), name='logout'),
    path('editar_usuario/', views.UsuarioUpdateView.as_view(), name='editar_usuario'),
    # Cambiar contraseña (cuando la sesión está iniciada)
    path('cambiar-password/', views.CustomPasswordChangeView.as_view(), name='cambiar_password'),
    path('cambiar-password/hecho/', views.CustomPasswordChangeDoneView.as_view(), name='password_change_done'),
]