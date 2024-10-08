from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Fotografo)
class FotografoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone')