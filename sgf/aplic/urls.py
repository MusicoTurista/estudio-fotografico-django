from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('fotografo', FotografoView.as_view(), name='fotografo'),
    path('evento', EventoView.as_view(), name='evento'),
    path('evento-detalhe/<int:id>/', EventoDetalheView.as_view(), name='evento-detalhe'),
]
