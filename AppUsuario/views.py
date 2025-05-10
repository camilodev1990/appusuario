# appusuario/AppUsuario/views.py

from django.shortcuts import render
from django.views.generic import FormView
from apps_importadas.appusuario.AppUsuario.models import Usuario
from apps_importadas.appusuario.AppUsuario.forms import UsuarioCreationForm, UsuarioLoginForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistroTemplateView(FormView):
    form_class = UsuarioCreationForm
    template_name = "registro.html"
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']        
        User.objects.create_user(email=email, password=password)
        return super().form_valid(form)



# vista de login por medio de un template 
class LoginTemplateView(LoginView):
    form_class = UsuarioLoginForm
    template_name = "login.html"
    success_url = reverse_lazy('home')
    redirect_authenticated_user = True

class LogoutTemplateView(LogoutView):
    template_name = 'logout.html'
    
    def get_success_url(self):
        return reverse_lazy('login')
    
    def get_context_data(self, **kwargs):
        # Añadimos el parámetro 'next' a la respuesta para redirigir al usuario al lugar correcto
        context = super().get_context_data(**kwargs)
        next_url = self.request.GET.get('next', '/')  # Si no hay 'next', redirige a la home
        context['next_url'] = next_url
        return context
    
'''
logout viene pensado como una plantilla de confirmacion 
entonces en el momento en el que el usuario no acepte cerrar sesion 
lo redirige a la pagina donde estaba, eso va en el next y si no hay next entonces lo lleva a la home

en la plantilla va asi configurada la linea 

<!-- logout.html -->

{% extends 'base.html' %}

{% block content %}
    <h2>¿Estás seguro que deseas cerrar sesión?</h2>
    <form method="post">
        {% csrf_token %}
        <button type="submit" class="btn btn-danger">Sí, cerrar sesión</button>
    </form>
    <!-- Usamos el parámetro next que fue agregado al contexto -->
    <a href="{{ next_url }}" class="btn btn-secondary">No, continuar</a>  <!-- Redirige a la página anterior si no desea cerrar sesión -->
{% endblock %}



'''