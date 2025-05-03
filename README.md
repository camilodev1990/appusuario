# AppUsuario

- Descripcion de la aplicacion :

pass


### Descarga

Para utilizarla se debe instalar como un submodulo y debe quedar adentro de una carpeta llamada apps_importadas, al ejecutar la siguiente linea dentro del proyecto django se creara la carpeta e instalara la app de forma automatica

`git submodule add https://github.com/camilodev1990/appusuario.git apps_importadas/appusuario`

Despues no olvidar inicializar el submodulo

`git submodule init`

Cuando quiera actualizar el submodulo

`git submodule update`

SI MAS ADELANTE REALIZO ALGUNA MODIFICACION EN EL MODELO USUARIO DEBO ACTUALIZAR EL MODULO ESTANDO DENTRO DEL PROYECTO QUE LO CONTENGA Y ME UBICO EN EL 

`git pull origin main`  # O la rama que estés utilizando



## settings - del proyecto



AUTH_USER_MODEL = "AppUsuario.Usuario"


INSTALLED_APPS = [
    ...
    'apps_importadas.appusuario.AppUsuario',
    'rest_framework',
    'rest_framework_simplejwt',
]





## urls.py - del proyecto

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('appusuario.AppUsuario.urls')),
]














