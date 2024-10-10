from django.contrib import admin
from .models import *
# Register your models here.


class EquipamentoInLine(admin.TabularInline):
    model = Equipamento

class FotoInLine(admin.TabularInline):
    model = Foto

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'descricao')

@admin.register(Fotografo)
class FotografoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone')
    inlines = [
        EquipamentoInLine
    ]

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')

@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'modelo')

@admin.register(CategoriaEvento)
class CategoriaEventoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'descricao')

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'data')

@admin.register(Entrega)
class EntregaAdmin(admin.ModelAdmin):
    list_display = ('evento', 'data')
    inlines = [
        FotoInLine
    ]