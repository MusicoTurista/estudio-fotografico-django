from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget,AdminTimeWidget

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True, label="Nome")
    last_name = forms.CharField(max_length=30, required=True, label="Sobrenome")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class EventRegistrationForm(forms.Form):

    data = forms.DateField(required=True, label="Data",widget=AdminDateWidget(attrs={'type': 'date'}))
    hora = forms.DateField(required=True, label="Hora",widget=AdminTimeWidget(attrs={'type': 'time'}))