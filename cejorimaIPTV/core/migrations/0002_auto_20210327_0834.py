# Generated by Django 3.1.7 on 2021-03-27 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Produto',
            new_name='Venda',
        ),
    ]