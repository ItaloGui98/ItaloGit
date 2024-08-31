from django.contrib import admin
from .models import Clube, Jogadores
# Register your models here.

@admin.register(Clube)
class ClubeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'AnoDeFundacao', 'vitorias', 'titulos')

@admin.register(Jogadores)
class JogadoresAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento', 'nacionalidade', 'posicao')

