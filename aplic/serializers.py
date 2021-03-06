from rest_framework import serializers

from aplic.models import Turma, Avaliacao, Nota, Usuario, Disciplina, Curso


class TurmaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Turma
        fields = '__all__'


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Avaliacao
        fields = '__all__'


class NotaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nota
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = '__all__'


class DisciplinaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Disciplina
        fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = '__all__'
