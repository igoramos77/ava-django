from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import IndexView, DisciplinaView, DisciplinaViewSet, NotaViewSet, AlunoViewSet, AvaliacaoiewSet

router = SimpleRouter()
router.register('alunos', AlunoViewSet)
router.register('disciplinas', DisciplinaViewSet)
router.register('notas', NotaViewSet)
router.register('avaliacoes', AvaliacaoiewSet)


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('disciplina/<int:id>', DisciplinaView.as_view(), name='disciplina'),
]
