from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('fotografo', FotografoView.as_view(), name='fotografo'),
]