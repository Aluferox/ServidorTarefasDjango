from django.urls import path
from .views import TarefaCreateView, ListaTarefaListView, TarefaUpdateView, TarefaDelete

urlpatterns = [
    path('criar_tarefas/', TarefaCreateView.as_view(), name='criar_tarefa'),
    path('', ListaTarefaListView.as_view(), name='lista_tarefa'),
    path('atualizar/<int:pk>/', TarefaUpdateView.as_view(), name='atualizar_tarefa'),
    path('deletar/<int:pk>/', TarefaDelete.as_view(), name='deletar_tarefa'),
]