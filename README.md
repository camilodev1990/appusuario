# appusuario
usuario personalizado

Para utilizar la aplicacion se debe tener en cuenta:

La aplicacion es para reutilizar entonces se crea una carpeta que se debe llamar apps_importadas y alli se descarga el repositorio


Agregar en settings 

AUTH_USER_MODEL = "AppUsuario.Usuario"


INSTALLED_APPS = [
    ...
    'apps_importadas.AppUsuario',
]

La aplicacion se debe instalar como un submodulo para poder trabajar con ella 

git submodule add https://github.com/camilodev1990/appusuario.git apps_importadas/appusuario

No olvidar inicializar el submodulo

git submodule init 

No olvidar actualizar el submodulo para trabajar con el 

git submodule update

SI MAS ADELANTE REALIZO ALGUNA MODIFICACION EN EL MODELO USUARIO DEBO ACTUALIZAR EL MODULO ESTANDO DENTRO DEL PROYECTO QUE LO CONTENGA Y ME UBICO EN EL 

git pull origin main  # O la rama que estés utilizando
















