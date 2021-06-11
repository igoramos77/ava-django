from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import IndexView, DisciplinaView, EstatisticasView, DisciplinaViewSet, NotaViewSet, UsuarioViewSet, AvaliacaoiewSet

router = SimpleRouter()
router.register('alunos', UsuarioViewSet)
router.register('disciplinas', DisciplinaViewSet)
router.register('notas', NotaViewSet)
router.register('avaliacoes', AvaliacaoiewSet)


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('disciplina/<int:id>', DisciplinaView.as_view(), name='disciplina'),
    path('estatisticas/', EstatisticasView.as_view(), name='estatisticas'),
]
