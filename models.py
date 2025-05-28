#apps_importadas/appusuario/models.py

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UsuarioManager
import uuid


class Usuario(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        editable=False,
        verbose_name="identificador",
    )

    email = models.EmailField(
        max_length=50, 
        unique=True,
        editable=True, 
        verbose_name="correo electronico", 
        help_text="correo electronico"        
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name="fecha de creacion"
    )

    fecha_modificacion = models.DateTimeField(
        auto_now=True,
        verbose_name="fecha de modificacion"
    )

    is_active = models.BooleanField(
        default=False,
        verbose_name="usuario activo"
    )

    is_staff = models.BooleanField(
        default=False,
        verbose_name="administrador"
    )

    is_superuser = models.BooleanField(
        default=False,
        verbose_name="superusuario"
    )


    objects = UsuarioManager()


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "USUARIO"
        verbose_name = "USUARIO"
        verbose_name_plural = "USUARIOS"
        ordering = ["-fecha_creacion"]
        indexes = [
            models.Index(fields=["email"], name="email_idx")
        ]

    def __str__(self):
        return self.email