# Generated by Django 3.1.7 on 2021-04-04 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210403_1655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venda',
            old_name='produto',
            new_name='dispositivo',
        ),
    ]
