# apps_importadas/appusuario/AppUsuario/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from apps_importadas.appusuario.AppUsuario.models import Usuario
from apps_importadas.appusuario.AppUsuario.validators import validar_password_segura


#----------------------------------------------------------------------------------------------------------
# registro de usuario
#----------------------------------------------------------------------------------------------------------
class UsuarioCreationForm(UserCreationForm):
    mostrar_contrasena = forms.BooleanField(
        required=False,
        label="Mostrar contraseña",
        widget=forms.CheckboxInput(attrs={
            'onclick': 'togglePasswordVisibility(this, "id_password1", "id_password2")'
        })
    )

    class Meta:
        model = Usuario
        fields = ['email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Correo electrónico'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'id': 'id_password1'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirmar contraseña',
            'id': 'id_password2'
        })
        self.fields['password1'].validators.append(validar_password_segura)

#----------------------------------------------------------------------------------------------------------
# login de usuario
#----------------------------------------------------------------------------------------------------------
class CustomLoginForm(AuthenticationForm):
    mostrar_contrasena = forms.BooleanField(
        required=False,
        label="Mostrar contraseña",
        widget=forms.CheckboxInput(attrs={
            'onclick': 'togglePasswordVisibility(this, "id_password")'
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Aquí se llama 'username', pero tú lo tratarás como 'email'
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Correo electrónico'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'id': 'id_password'
        })

#----------------------------------------------------------------------------------------------------------
# logout de usuario
#----------------------------------------------------------------------------------------------------------
class ConfirmLogoutForm(forms.Form):
    confirmar = forms.BooleanField(
        required=True,
        label="Confirmo que deseo cerrar sesión",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

#----------------------------------------------------------------------------------------------------------
# cambiar contraseña sesion iniciada
#----------------------------------------------------------------------------------------------------------
class CustomPasswordChangeForm(PasswordChangeForm):
    mostrar_contrasena = forms.BooleanField(
        required=False,
        label="Mostrar contraseña",
        widget=forms.CheckboxInput(attrs={
            'onclick': 'togglePasswordVisibility(this, "id_old_password", "id_new_password1", "id_new_password2")'
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contraseña actual',
            'id': 'id_old_password'
        })
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nueva contraseña',
            'id': 'id_new_password1'
        })
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirmar nueva contraseña',
            'id': 'id_new_password2'
        })

        # Validación adicional (opcional)
        self.fields['new_password1'].validators.append(validar_password_segura)


#----------------------------------------------------------------------------------------------------------
# modificar usuario
#----------------------------------------------------------------------------------------------------------
class UsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email']  # Agrega más campos si tu modelo los tiene, como 'first_name', 'last_name'
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Correo electrónico'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Si hay más campos, puedes personalizar sus widgets aquí
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'