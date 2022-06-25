from django.contrib import admin
from .models import Desafio, User

@admin.register(Desafio)
class DesafioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'dataCriacao', 'grandeIdeia', 'questaoEssencial', 'desafios', 'documentosEnvolver',
                    'questoesNorteadoras', 'recursos', 'atividades', 'sintese', 'documentosInvestigar',
                    'conceitosSolucao', 'implementacaoSolucao', 'avaliacao', 'documentosAgir', 'usuario')

