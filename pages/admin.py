from django.contrib import admin
from .models import Aplicativo, Tag


@admin.register(Aplicativo)
class AplicativoModelAdmin(admin.ModelAdmin):
    list_display = ['criado', 'ativo', 'titulo', 'descricao', 'categoria']
    search_fields = ['criado', 'ativo', 'titulo']


@admin.register(Tag)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']