# Generated by Django 4.0.1 on 2022-01-30 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_projeto', models.CharField(max_length=150)),
                ('data_inicio', models.IntegerField()),
                ('data_termino', models.IntegerField()),
                ('valor_projeto', models.IntegerField()),
                ('risco', models.CharField(max_length=100)),
                ('participantes', models.CharField(max_length=150)),
            ],
        ),
    ]
