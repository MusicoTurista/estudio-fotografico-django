from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

from django.contrib import messages
# Create your views here.

from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

class FotografoView(TemplateView):
    template_name = 'fotografo.html'
    def get_context_data(self, **kwargs):
        context = super(FotografoView, self).get_context_data(**kwargs)
        context['fotografos'] = Fotografo.objects.order_by('-nome').all()
        return context

class EventoView(TemplateView):
    template_name = 'evento.html'
    def get_context_data(self, **kwargs):
        context = super(EventoView, self).get_context_data(**kwargs)
        context['eventos'] = CategoriaEvento.objects.order_by('-tipo').all()
        return context

class EventoDetalheView(TemplateView):
    template_name = 'evento-detalhe.html'
    def get_context_data(self, **kwargs):
        context = super(EventoDetalheView, self).get_context_data(**kwargs)
        id = self.kwargs['id']
        context['evento'] = CategoriaEvento.objects.filter(id=id).first
        return context

class EventoContratoView(TemplateView):
    template_name = 'evento-contrato.html'
    def get_context_data(self, **kwargs):
        context = super(EventoContratoView, self).get_context_data(**kwargs)
        id = self.kwargs['id']
        tipo = self.kwargs['tipo']
        if tipo == 'pacotefoto' or tipo == 'pacotehora':
            context['evento'] = CategoriaEvento.objects.filter(id=id).first
            context['tipo'] = tipo
            context['form'] = EventRegistrationForm()
            return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():


def RegisterView(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registrado com sucesso.")
            return redirect('/users/login')
    else:
        form = UserRegistrationForm()
    return render(request,"users/register.html",{'form':form})

def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bem vindo, {username}!")
                return redirect('/')
            else:
                messages.warning(request, "Username ou senha invalidos.")
        else:
            messages.warning(request, "Username ou senha invalidos.")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def LogoutView(request):
    logout(request)
    return redirect('/users/login')
