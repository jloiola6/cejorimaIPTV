# Generated by Django 3.1.7 on 2021-03-27 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, verbose_name='Nome')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('endereco', models.CharField(max_length=150, verbose_name='Endereço')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, verbose_name='Nome')),
                ('usuario', models.CharField(max_length=10, verbose_name='Nome de Usuário')),
                ('senha', models.CharField(max_length=15, verbose_name='Senha')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('adm', models.CharField(blank=True, max_length=1, null=True, verbose_name='Adm')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
        ),
    ]
