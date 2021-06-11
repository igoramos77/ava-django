from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import TemplateView, ListView
from django_weasyprint import WeasyTemplateView
from weasyprint import HTML

from .models import Turma, Avaliacao, Nota, Usuario, Disciplina, Curso, Configuracoes

from rest_framework import permissions

from . import serializers

from aplic.serializers import NotaSerializer, UsuarioSerializer, DisciplinaSerializer, AvaliacaoSerializer
from rest_framework import viewsets


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        #    PEGA O USUARIO LOGADO
        context['user'] = Usuario.objects.get(matricula=self.request.user)

        # PEGA O ANO CURRENTE
        context['ano_currente'] = Configuracoes.objects.values_list('ano_currente', flat=True).first()

        # PEGA O SEMESTRE CURRENTE
        context['semestre_currente'] = Configuracoes.objects.values_list('semestre_currente', flat=True).first()

        context['turmas'] = Turma.objects.filter(alunos__matricula=context['user'], ano=context['ano_currente'], semestre=context['semestre_currente'], periodo=5) \
            .order_by('dia_da_semana').all()

        context['avaliacao_length'] = Avaliacao.objects.filter(tipo='Prova').count()
        context['trabalho_length'] = Avaliacao.objects.filter(tipo='Trabalho').count()
        context['notas_lancadas'] = Nota.objects.filter(aluno=context['user']).count()

        context['week'] = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']

        return context

    def get_avaliacao_length(self, **kwargs):
        avaliacao_length = super(IndexView, self).get_context_data(**kwargs)
        avaliacao_length['avaliacao_length'] = Avaliacao.objects.filter(tipo='Prova').count()

        return avaliacao_length

    def get_trabalho_length(self, **kwargs):
        trabalho_length = super(IndexView, self).get_context_data(**kwargs)
        trabalho_length['trabalho_length'] = Avaliacao.objects.filter(tipo='Trabalho').count()

        return trabalho_length


class DisciplinaView(TemplateView):
    template_name = 'disciplina.html'

    def get_context_data(self, **kwargs):
        context = super(DisciplinaView, self).get_context_data(**kwargs)
        context['turma'] = Turma.objects.get(id=kwargs['id'])
        context['avaliacoes'] = Avaliacao.objects.filter(turma_id=context['turma'], tipo='Prova')
        context['trabalhos'] = Avaliacao.objects.filter(turma_id=context['turma'], tipo='Trabalho')

        return context


class EstatisticasView(ListView):
    template_name = 'estatisticas.html'
    paginate_by = 1
    ordering = ['id']
    model = Nota

    def get_context_data(self, **kwargs):
        context = super(EstatisticasView, self).get_context_data(**kwargs)

        context['user'] = Usuario.objects.get(matricula=self.request.user)

        context['avaliacoes'] = Nota.objects.filter(aluno=context['user']).order_by('create_at').all()

        context['notas_semestre'] = Nota.objects.values_list('valor', flat=True).filter(aluno=context['user']).order_by('-create_at')
        context['disciplinas_semestre'] = Nota.objects.values_list('turma__disciplina__nome', flat=True).filter(aluno=context['user']).order_by('-create_at')

        return context


class RelatorioNotasView(WeasyTemplateView):

    def get(self, request, *args, **kwargs):
        notas = Nota.objects.order_by('create_at')

        html_string = render_to_string('relatorio-notas.html', {'notas': notas})

        html = HTML(string=html_string, base_url=request.build_absolute_uri())
        html.write_pdf(target='/tmp/relatorio-notas.pdf')
        fs = FileSystemStorage('/tmp')

        with fs.open('relatorio-notas.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="relatorio-notas.pdf"'
        return response


#   VIEWSETS ----------------------------------------------------------------------------------------------------------

class DisciplinaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)

    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class NotaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)

    queryset = Nota.objects.all()
    serializer_class = NotaSerializer


class AvaliacaoiewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)

    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

