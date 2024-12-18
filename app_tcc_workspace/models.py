from django.db import models
from django.contrib.auth.models import User  # Assumindo que você usa o User padrão do Django
from app_forms.models import TCC
from app_tcc.models import Aluno, Orientador, Curso

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relaciona a mensagem ao usuário
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    tcc = models.ForeignKey(TCC, on_delete=models.CASCADE, related_name="messages", default=1)

    def __str__(self):
        return f"{self.user.username}: {self.content[:20]} ({self.timestamp})"
    

class Task(models.Model):
    tcc = models.ForeignKey(TCC, related_name='tasks', on_delete=models.CASCADE)  # Relacionamento com TCC
    title = models.CharField(max_length=255)  # Título da tarefa
    description = models.TextField(blank=True, null=True)  # Descrição opcional da tarefa
    completed = models.BooleanField(default=False)  # Se a tarefa está concluída ou não
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação da tarefa
    updated_at = models.DateTimeField(auto_now=True)  # Data da última atualização da tarefa
    due_date = models.DateField(blank=True, null=True)  # Data de vencimento opcional

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
