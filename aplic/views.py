from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Turma, Avaliacao, Nota, Aluno, Disciplina, Curso

from rest_framework import permissions

from . import serializers

from aplic.serializers import NotaSerializer, AlunoSerializer, DisciplinaSerializer, AvaliacaoSerializer
from rest_framework import viewsets


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['user'] = Aluno.objects.get(id='1')

        context['turmas'] = Turma.objects.filter(alunos__id='1', ano='2021', semestre='1', periodo='5')\
            .order_by('dia_da_semana').all()

        context['avaliacao_length'] = Avaliacao.objects.filter(tipo='Prova').count()
        context['trabalho_length'] = Avaliacao.objects.filter(tipo='Trabalho').count()
        context['notas_lancadas'] = Nota.objects.filter(aluno='1').count()

        context['week'] = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira',
                           'Sábado']

        return context

    #   perguntar se nao posso implementar métodose passa-los para a view
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


#   VIEWSETS ----------------------------------------------------------------------------------------------------------

class DisciplinaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)

    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class NotaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)

    queryset = Nota.objects.all()
    serializer_class = NotaSerializer


class AvaliacaoiewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)

    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

