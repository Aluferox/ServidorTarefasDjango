from django.db import models
from django.contrib.auth.models import User


class Tarefa(models.Model):
    alta = 'alta'
    media = 'média'
    baixa = 'baixa'
    PRIORIDADES = [
        (alta, 'alta'),
        (media,'media'),
        (baixa, 'baixa')
    ]

    STATUS_TASK_CHOICE = [
        ('em andamento', 'em andamento'),
        ('pendente', 'pendente'),
        ('concluída', 'concluída')
    ]

    tarefa = models.CharField(max_length=200)
    prioridade = models.CharField(choices=PRIORIDADES, max_length=5)
    status = models.CharField(choices=STATUS_TASK_CHOICE, max_length=12, default='em andamento')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.tarefa
