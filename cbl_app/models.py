from django.db import models
from django.contrib.auth.models import User


class Desafio(models.Model):
    titulo = models.CharField('Título', max_length=200)
    dataCriacao = models.DateTimeField('Data de criação', auto_now=True)
    grandeIdeia = models.TextField('A Grande Ideia (Tema)', default='Não concluído.', help_text='Exemplos de grandes ideias incluem Comunidade, Empoderamento Social, Criatividade, Saúde, Sustentabilidade e Democracia.')
    questaoEssencial = models.TextField('Questão Essencial (Pergunta)', default='Não concluído.', help_text='Por exemplo: O que preciso fazer para ser mais saudável?')
    desafios = models.TextField('O Desafio (Solução)', default='Não concluído.', help_text='É a solução para a questão levantada, deve ser imediata e possível de realizar.')
    documentosEnvolver = models.FileField('Materiais Auxiliadores - Etapa Envolver', blank=True, help_text='Adicione aqui arquivos de materiais da etapa 1 que considerar agregadores ao desafio.', upload_to='uploads/')
    questoesNorteadoras = models.TextField('Questões Norteadoras (Perguntas guias)', default='Não concluído.', help_text='Questões relacionadas com o desafio, é importante fazer variadas perguntas sobre o tema definido.')
    recursos = models.TextField('Recursos orientadores', default='Não concluído.', help_text='Exemplos de recursos orientadores incluem: conteúdo online e cursos, bancos de dados, livros didáticos e redes sociais.')
    atividades = models.TextField('Atividades orientadoras', default='Não concluído.', help_text='Exemplos de atividades orientadoras incluem: simulações, experimentos, projetos, conjuntos de problemas, pesquisa e jogos.')
    sintese = models.TextField('Síntese avaliadora', default='Não concluído.', help_text='A análise das lições aprendidas durante as questões guias, recursos e atividades.')
    documentosInvestigar = models.FileField('Materiais Auxiliadores - Etapa Investigar', blank=True, help_text='Adicione aqui arquivos de materiais da etapa 2 que considerar agregadores ao desafio.', upload_to='uploads/')
    conceitosSolucao = models.TextField('Conceitos de Solução', default='Não concluído.', help_text='Podem envolver planos para uma campanha para informar ou educar, projetos de melhoria da escola ou da Comunidade, desenvolvimento de produtos ou outras atividades.')
    implementacaoSolucao = models.FileField('Implementação da Solução', blank=True, help_text='Após a aprovação do conceito de solução, os aprendizes desenvolvem protótipos, experimentos e testes.', upload_to='uploads/')
    avaliacao = models.TextField('Avaliação final', default='Não concluído.', help_text='Hora de medir os resultados, refletir sobre o que funcionou e o que não e determinar o seu impacto sobre o desafio.')
    documentosAgir = models.FileField('Materiais Auxiliadores - Etapa Agir', blank=True, help_text='Adicione aqui arquivos de materiais da etapa 3 que considerar agregadores ao desafio.', upload_to='uploads/')
    usuario = models.ForeignKey(User, related_name='desafios', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Desafio'
        verbose_name_plural = 'Desafios'
        ordering = ['dataCriacao']

    def __str__(self):
        return self.titulo