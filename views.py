# appusuario/AppUsuario/views.py
from django.views.generic.edit import CreateView, UpdateView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth import get_user_model, logout
from django.contrib import messages
from django.shortcuts import redirect, render

from apps_importadas.appusuario.forms import UsuarioCreationForm, CustomLoginForm, CustomPasswordChangeForm, UsuarioUpdateForm, ConfirmLogoutForm
from apps_importadas.appusuario.models import Usuario


usuario = get_user_model()

#----------------------------------------------------------------------------------------------------------
# registro de usuario
#----------------------------------------------------------------------------------------------------------
class RegistroUsuarioView(CreateView):
    model = Usuario
    form_class = UsuarioCreationForm
    template_name = 'usuario/registro.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        usuario = form.save(commit=False)
        usuario.is_active = True  # Activar temporalmente ------------------------
        usuario.save()
        return super().form_valid(form)

#----------------------------------------------------------------------------------------------------------
# login de usuario
#----------------------------------------------------------------------------------------------------------
class CustomLoginView(LoginView):
    template_name = 'usuario/login.html'
    authentication_form = CustomLoginForm

#----------------------------------------------------------------------------------------------------------
# logout de usuario
#----------------------------------------------------------------------------------------------------------
class ConfirmLogoutView(View):
    template_name = 'usuario/logout-confirmar.html'

    def get(self, request):
        form = ConfirmLogoutForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ConfirmLogoutForm(request.POST)
        if form.is_valid():
            logout(request)
            return redirect('login')
        return render(request, self.template_name, {'form': form})
    
#----------------------------------------------------------------------------------------------------------
# cambiar contraseña sesion iniciada
#----------------------------------------------------------------------------------------------------------
class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuario/cambiar_password.html'
    success_url = reverse_lazy('password_change_done')  
    form_class = CustomPasswordChangeForm

class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'usuario/password_change_done.html'   

#----------------------------------------------------------------------------------------------------------
# modificar usuario
#----------------------------------------------------------------------------------------------------------

class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    form_class = UsuarioUpdateForm
    template_name = 'usuario/editar.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Tu perfil ha sido actualizado correctamente.")
        return super().form_valid(form)