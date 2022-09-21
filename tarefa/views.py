from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tarefa
from django.urls import reverse_lazy


class TarefaCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Tarefa
    fields = ['tarefa', 'prioridade', 'status']
    template_name_suffix = '_create'
    success_url = reverse_lazy('lista_tarefa')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)



class ListaTarefaListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Tarefa

    def get_queryset(self):
        user = self.request.user
        return Tarefa.objects.filter(user=user)



class TarefaUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Tarefa
    fields = ['tarefa', 'prioridade', 'status', 'is_active']
    success_url = reverse_lazy('lista_tarefa')
    template_name_suffix = '_update_form'



class TarefaDelete(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Tarefa
    success_url = reverse_lazy('lista_tarefa')
