from django.contrib.auth.models import BaseUserManager
from django.core.mail import send_mail
from django.conf import settings
from .utils.jwt_tools import generar_token_reset_password


class UsuarioManager(BaseUserManager):


    #----------------------------------------------------------------------------------------
    #crear usuario 

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El usuario debe tener un correo electrónico")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    #----------------------------------------------------------------------------------------
    # crear superusuario

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("El superusuario debe tener is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("El superusuario debe tener is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

    #----------------------------------------------------------------------------------------
    # reestablecer contraseña sin sesion iniciada utilizando tokens drf

    