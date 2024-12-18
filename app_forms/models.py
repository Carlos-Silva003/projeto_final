from django.db import models
from app_tcc.models import Aluno, Orientador, Curso


class TCC(models.Model):
    STATUS_CHOICES = [
        ('em_andamento', 'Em Andamento'),
        ('submetido', 'Submetido'),
        ('aprovado', 'Aprovado'),
        ('reprovado', 'Reprovado'),
    ]

    titulo = models.CharField(max_length=200)
    capa = models.ImageField(upload_to='capas/')
    descricao = models.TextField()
    autores = models.ManyToManyField(Aluno, limit_choices_to={'ativo': True})
    orientador = models.ForeignKey(Orientador, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_entrega = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='em_andamento')

    def __str__(self):
        return self.titulo
