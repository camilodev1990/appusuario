from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import Usuario
from django.contrib.auth import authenticate
from .validators import validar_password_segura


class UsuarioCreationForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'autocomplete': 'email',
                'placeholder': 'Ingresa tu correo electrónico',
                'id': 'emailregistro'
            }
        )
    )
    
    password1 = forms.CharField(
        required=True,
        min_length=8,
        validators=[validar_password_segura],
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'placeholder': 'Ingresa una contraseña',
                'id': 'password1registro'
            }
        ),
        error_messages={
            'required': 'La contraseña es obligatoria.',
            'min_length': 'Debe contener 8 caracteres minimo'
        }
    )
    
    password2 = forms.CharField(
        required=True,
        min_length=8,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'placeholder': 'Repite la contraseña',
                'id': 'password2registro'
            }
        ),
        error_messages={
            'required': 'La confirmación de contraseña es obligatoria.',
            'min_length': 'Debe contener 8 caracteres minimo'
        }
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2

#-------------------------------------------------------------------------------------------------------------


# formulario que me permite encampos el frontend y en el admin modificar un usuario
class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['email', 'is_active', 'is_staff', 'is_superuser']


class UsuarioLoginForm(forms.Form):

    #campo email contiene un input tipo email y atributo autocompletar y placeholder
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'autocomplete':'email',
                'placeholder':'ingresa tu correo electronico'
            }
        )
    )


    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'autocomplete':'current-password',
                'placeholder':'ingresa tu contraseña'
            }
        )
    )


    # clean es un metodo de la clase heredada Form 
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            # Usamos authenticate para validar usuario y contraseña
            usuario = authenticate(email=email, password=password)
            if usuario is None:
                raise forms.ValidationError("Correo o contraseña incorrectos.")
            if not usuario.is_active:
                raise forms.ValidationError("Esta cuenta está desactivada.")
            
            # Guardamos el usuario validado en el formulario
            self.user = usuario

        return cleaned_data