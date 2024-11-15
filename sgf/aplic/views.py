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
