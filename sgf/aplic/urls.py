from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    #path('contato', ContatoView.as_view(), name='contato'),
    #path('sobre', SobreView.as_view(), name='sobre'),
]