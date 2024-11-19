from django.shortcuts import render
from .models import *
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
