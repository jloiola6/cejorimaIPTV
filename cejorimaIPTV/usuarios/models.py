from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField('Nome', max_length=40)
    usuario = models.CharField('Nome de Usuário', max_length=10)
    senha = models.CharField('Senha', max_length=15)
    telefone = models.CharField('Telefone', max_length=15)
    adm = models.CharField('Adm', max_length=1, null=True, blank=True)

    create_at = models.DateTimeField('Criado em', auto_now_add= True)
    updated_at = models.DateTimeField('Atualizado em', auto_now= True)

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=40)
    telefone = models.CharField('Telefone', max_length=15)
    endereco = models.CharField('Endereço', max_length= 150)

    def __str__(self):
        return self.nome
    