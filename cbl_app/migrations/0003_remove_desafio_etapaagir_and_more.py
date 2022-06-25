# Generated by Django 4.0.4 on 2022-06-25 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbl_app', '0002_alter_desafio_etapaagir_alter_desafio_etapaenvolver_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='desafio',
            name='etapaAgir',
        ),
        migrations.RemoveField(
            model_name='desafio',
            name='etapaEnvolver',
        ),
        migrations.RemoveField(
            model_name='desafio',
            name='etapaInvestigar',
        ),
        migrations.AddField(
            model_name='desafio',
            name='atividades',
            field=models.TextField(default='Não concluído.', help_text='Exemplos de atividades orientadoras incluem: simulações, experimentos, projetos, conjuntos de problemas, pesquisa e jogos.', verbose_name='Atividades orientadoras'),
        ),
        migrations.AddField(
            model_name='desafio',
            name='avaliacao',
            field=models.TextField(default='Não concluído.', help_text='Hora de medir os resultados, refletir sobre o que funcionou e o que não e determinar o seu impacto sobre o desafio.', verbose_name='Avaliação final'),
        ),
        migrations.AddField(
            model_name='desafio',
            name='conceitosSolucao',
            field=models.TextField(default='Não concluído.', help_text='Podem envolver planos para uma campanha para informar ou educar, projetos de melhoria da escola ou da Comunidade, desenvolvimento de produtos ou outras atividades.', verbose_name='Conceitos de Solução'),
        ),
        migrations.AddField(
            model_name='desafio',
            name='desafios',
            field=models.TextField(default='Não concluído.', help_text='É a solução para a questão levantada, deve ser imediata e possível de realizar.', verbose_name='O Desafio (Solução)'),
        ),
        migrations.AddField(
            model_name='desafio',
            name='documentosAgir',
            field=models.FileField(blank=True, help_text='Adicione aqui arquivos de materiais da etapa 3 que considerar agregadores ao desafio.', upload_to='uploads/', verbose_name='Materiais Auxiliadores - Etapa Agir'),
        ),
        migrations.AddField(
            model_name='desafio',
            name='documentosEnvolver',
            field=models.FileField(blank=True, help_text='Adicione aqui arquivos de materiais da etapa 1 que considerar agregadores ao desafio.', upload_to='uploads/', verbose_name='Materiais Auxiliadores - Etapa Envolver'),
        ),
        migrations.AddField(
            model_name='desafio',
            name='documentosInvestigar',
            field=models.FileField(blank=True, help_text='Adicione aqui arquivos de materiais da etapa 2 que considerar agregadores ao desafio.', upload_to='uploads/', verbose_name='Materiais Auxiliadores - Etapa Investigar'),
        ),
        migrations.AddField(
            model_name='desafio',
            name='grandeIdeia',
            field=models.TextField(default='Não concluído.', help_text='Exemplos de grandes ideias incluem Comunidade, Empoderamento Social, Criatividade, Saúde, Sustentabilidade e Democracia.', verbose_name='A Grande Ideia (Tema)'),
        ),
        migrations.AddField(
            model_name='desafio',
            name='implementacaoSolucao',
            field=models.FileField(blank=True, help_text='Após a aprovação do conceito de solução, os aprendizes desenvolvem protótipos, experimentos e testes.', upload_to='uploads/', verbose_name='Implementação da Solução'),
        ),
        migrations.AddField(
            model_name='desafio',
            name='questaoEssencial',
            field=models.TextField(default='Não concluído.', help_text='Por exemplo: O que preciso fazer para ser mais saudável?', verbose_name='Questão Essencial (Pergunta)'),
        ),
        migrations.AddField(
            model_name='desafio',
            name='questoesNorteadoras',
            field=models.TextField(default='Não concluído.', help_text='Questões relacionadas com o desafio, é importante fazer variadas perguntas sobre o tema definido.', verbose_name='Questões Norteadoras (Perguntas guias)'),
        ),
        migrations.AddField(
            model_name='desafio',
            name='recursos',
            field=models.TextField(default='Não concluído.', help_text='Exemplos de recursos orientadores incluem: conteúdo online e cursos, bancos de dados, livros didáticos e redes sociais.', verbose_name='Recursos orientadores'),
        ),
        migrations.AddField(
            model_name='desafio',
            name='sintese',
            field=models.TextField(default='Não concluído.', help_text='A análise das lições aprendidas durante as questões guias, recursos e atividades.', verbose_name='Síntese avaliadora'),
        ),
        migrations.DeleteModel(
            name='EtapaAgir',
        ),
        migrations.DeleteModel(
            name='EtapaEnvolver',
        ),
        migrations.DeleteModel(
            name='EtapaInvestigar',
        ),
    ]
