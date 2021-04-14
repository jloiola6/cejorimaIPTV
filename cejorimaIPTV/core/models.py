from django.db import models
from ..usuarios.models import Cliente

# Create your models here.

# class Venda(models.Model):
#     tipo = models.CharField('Tipo', max_length=15, choices=(('Box','Box'),('TV','TV'), ('Celular','Celular')), default='Box')
#     marca = models.CharField('Marca', max_length=30, blank=True, null=True)
#     device_ID = models.CharField('Device ID', max_length=20, blank=True, null=True)
#     device_KEY = models.CharField('Device KEY', max_length=20, blank=True, null=True)
#     cliente = models.CharField('Cliente', max_length=50, blank=True, null=True)
#     # cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)
#     situacao = models.CharField('Situação', max_length=15, choices=(('Vendido','Vendido'),('Estoque','Estoque'), ('Defeito','Defeito')), default='Estoque')
#     pagamento = models.CharField('Pagamento', max_length=15, choices=(('50%','50%'),('100%','100%')), default='100%')
#     app = models.CharField('App', max_length=15, choices=(('OK','OK'),('Grátis','Grátis'), ('50%','50%')), default='Ok')

#     create_at = models.DateTimeField('Criado em', auto_now_add= True)
#     updated_at = models.DateTimeField('Atualizado em', auto_now= True)

#     def __str__(self):
#         return self.name


class Dispositivos(models.Model):
    nome = models.CharField('Nome', max_length=100, blank=True)
    device_ID = models.CharField('Device ID', max_length=20, blank=True, null=True)
    device_KEY = models.CharField('Device KEY', max_length=20, blank=True, null=True)
    situacao = models.CharField('Situação', max_length=15, choices=(('Vendido','Vendido'),('Estoque','Estoque'), ('Defeito','Defeito'), ('Comprador', 'Comprador')), default='Estoque')

    create_at = models.DateTimeField('Criado em', auto_now_add= True)
    updated_at = models.DateTimeField('Atualizado em', auto_now= True)

    def __str__(self):
        return self.nome

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)
    produto = models.ForeignKey(Dispositivos, on_delete=models.CASCADE, blank=True)
    tipo = models.CharField('Tipo', max_length=15, choices=(('Box','Box'),('TV','TV'), ('Celular','Celular')), default='Box')
    pagamento = models.CharField('Pagamento', max_length=15, choices=(('50%','50%'),('100%','100%')), default='100%')
    aplicativo = models.CharField('App', max_length=15, choices=(('OK','OK'),('Grátis','Grátis'), ('50%','50%')), default='Ok')

    create_at = models.DateTimeField('Criado em', auto_now_add= True)
    updated_at = models.DateTimeField('Atualizado em', auto_now= True)
