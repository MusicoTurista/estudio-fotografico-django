from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget,AdminTimeWidget
from django.contrib import messages
from .models import Evento
import datetime
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True, label="Nome")
    last_name = forms.CharField(max_length=30, required=True, label="Sobrenome")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class EventRegistrationForm(forms.Form):

    data_evento = forms.DateField(required=True, label="Data",widget=AdminDateWidget(attrs={'type': 'date'}))
    hora_evento = forms.DateField(required=True, label="Hora",widget=AdminTimeWidget(attrs={'type': 'time'}))

    def is_valid(self, data=None, request=None):
        if data is None or request is None:
            return False
        date = data['data_evento']
        hour = data['hora_evento']
        date_hour =f"{date}/{hour}"
        date_hour = datetime.datetime.strptime(date_hour, '%Y-%m-%d/%H:%M')
        if date_hour < datetime.datetime.now() + datetime.timedelta(hours=3):
            messages.warning(request, f"Só é possivel marcar um evento a partir de {datetime.datetime.now() + datetime.timedelta(hours=3)}")
            return False
        try:
            evento = Evento.objects.get(data__istartswith=date)
            messages.warning(request, "Este dia já está ocupado.")
            return False
        except Evento.DoesNotExist:
            return True
