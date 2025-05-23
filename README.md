# 🧩 AppUsuario

Aplicación Django desarrollada por **camilodev1990@gmail.com** que permite:

- Registro de usuarios con contraseña segura
- Inicio de sesión
- Cierre de sesión
- Edición de datos del usuario
- Modelo de usuario personalizado con UUID

---

## 🚀 Instalación

Agrega esta app como submódulo dentro de tu proyecto:

```bash
git submodule add https://github.com/camilodev1990/appusuario.git apps_importadas/appusuario
git submodule init
```
⚠️ Si realizas cambios en el modelo Usuario o deseas actualizar el submódulo:
```
cd apps_importadas/appusuario
git pull origin main
git stash
```

⚙️ Configuración en settings.py

```
import os


INSTALLED_APPS = [
    # AppUsuario
    'apps_importadas.appusuario.AppUsuario',
]


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, 'templates'),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# Usuario personalizado
AUTH_USER_MODEL = "AppUsuario.Usuario"

# Redirecciones de login/logout
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'login'

# Archivos estáticos
STATIC_URL = "static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

```

🧭 Configuración en urls.py del proyecto

```
from django.contrib import admin
from django.urls import path, include
from proyectoprueba import views  # cuidado con el nombre del proyecto

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.HomeView.as_view(), name="home"),
    path("usuario/", include("apps_importadas.appusuario.AppUsuario.urls")),
]

```

DENTRO DEL PROYECTO SE DEBE CREAR DOS CARPETAS 

🧪 Templates que debes crear

Crea las siguientes plantillas HTML en la carpeta templates/:

registro.html

login.html

logout.html

editar_usuario.html

recuperar_contraseña.html

home.html



## static
css y js de las plantillas del proyecto


```
proyectoprueba/
├── apps_importadas/
│   └── appusuario/
│       └── AppUsuario/
├── templates/
│   ├── registro.html
│   ├── login.html
│   ├── logout.html
│   ├── editar_usuario.html
│   └── recuperar_contraseña.html
├── static/
│   ├── css/
│   └── js/
├── manage.py
└── settings.py
```