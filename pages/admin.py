from django.contrib import admin
from .models import Aplicativo


@admin.register(Aplicativo)
class AplicativoModelAdmin(admin.ModelAdmin):
    list_display = ['criado', 'ativo', 'titulo', 'descricao', 'categoria']
    search_fields = ['criado', 'ativo', 'titulo']