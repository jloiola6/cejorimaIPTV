# Generated by Django 3.1.7 on 2021-04-14 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20210414_0557'),
        ('core', '0008_auto_20210414_0726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='produto',
        ),
        migrations.AddField(
            model_name='venda',
            name='box',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.box'),
        ),
        migrations.AlterField(
            model_name='venda',
            name='cliente',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.cliente'),
        ),
    ]