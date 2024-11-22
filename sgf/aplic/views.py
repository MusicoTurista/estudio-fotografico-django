from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.views import View
from django.contrib import messages
from django.views.generic import TemplateView
# Create your views here.


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

def EventoContratoView(request, **kwargs):
    tipo = kwargs['tipo']
    evento = CategoriaEvento.objects.filter(id=kwargs['id']).first
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid(data=request.POST,request=request):
                date = request.POST['data_evento']
                hour = request.POST['hora_evento']

                current_user = request.user
                data = f'{date} {hour}'
                categoria_id = kwargs['id']
                evento = CategoriaEvento.objects.get(id=categoria_id)
                pacote_tipo = 'Quantidade de fotos' if tipo == 'pacotefoto' else 'Tempo de serviço'

                novo_evento = Evento(cliente=current_user, data=data, categoria=evento, pacote_tipo=pacote_tipo)
                novo_evento.save()
                messages.success(request, "Evento requisitado com sucesso!")
                return redirect(f'/evento-detalhe/{kwargs["id"]}')
    else:
        form = EventRegistrationForm
    return render(request, 'evento-contrato.html', {'form': form, 'tipo': tipo, 'evento': evento})
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
