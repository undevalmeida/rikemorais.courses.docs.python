from django.contrib import admin
from .models import Receita


class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'pessoa', 'nome_receita', 'categoria',
                    'tempo_preparo', 'publicada')
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_editable = ('publicada', 'tempo_preparo', 'pessoa', 'categoria')
    list_per_page = 50


admin.site.register(Receita, ListandoReceitas)
