# Generated by Django 3.1.7 on 2021-03-27 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210327_0928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='nome',
        ),
    ]