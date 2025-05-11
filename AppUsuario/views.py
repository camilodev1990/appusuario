# appusuario/AppUsuario/views.py

from django.shortcuts import render
from django.views.generic import FormView
from apps_importadas.appusuario.AppUsuario.models import Usuario
from apps_importadas.appusuario.AppUsuario.forms import UsuarioCreationForm, UsuarioLoginForm, UsuarioChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

User = get_user_model()

#----------------------------------------------------------------------------------------------------------
class RegistroTemplateView(FormView):
    form_class = UsuarioCreationForm
    template_name = "registro.html"
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']        
        User.objects.create_user(email=email, password=password)
        return super().form_valid(form)


#----------------------------------------------------------------------------------------------------------

class LoginTemplateView(LoginView):
    form_class = UsuarioLoginForm
    template_name = "login.html"
    success_url = reverse_lazy('home')
    redirect_authenticated_user = True


#----------------------------------------------------------------------------------------------------------

class LogoutTemplateView(LogoutView):
    next_page = reverse_lazy('login') 

#----------------------------------------------------------------------------------------------------------

class UsuarioUpdateTemplateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    form_class = UsuarioChangeForm
    template_name = 'editar_usuario.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user  