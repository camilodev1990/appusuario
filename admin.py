#apps_importadas/appusuario/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Usuario
from .forms import UsuarioCreationForm, UsuarioUpdateForm


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    add_form = UsuarioCreationForm
    form = UsuarioUpdateForm
    model = Usuario
    list_display = ("email", "is_active", "is_staff", "is_superuser", "fecha_creacion")
    list_filter = ("is_active", "is_staff", "is_superuser")
    ordering = ("-fecha_creacion",)
    search_fields = ("email",)

    fieldsets = (
        (_("Información de acceso"), {"fields": ("email", "password")}),
        (_("Permisos"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        (_("Fechas"), {"fields": ("fecha_creacion", "fecha_modificacion")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "is_active", "is_staff", "is_superuser", "groups", "user_permissions"),
        }),
    )
