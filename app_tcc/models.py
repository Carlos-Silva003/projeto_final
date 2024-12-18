from django.db import models
from django.contrib.auth.models import User  # Importando o modelo User

from django.db import models
from django.contrib.auth.models import User  # Importando o modelo User

class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relacionamento com User
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)  # Relacionamento com Curso
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

class Orientador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relacionamento com User
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
