# Generated by Django 4.0.1 on 2022-01-31 03:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_alter_cadastro_data_inicio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='data_inicio',
            field=models.DateField(default=datetime.datetime(2022, 1, 31, 3, 31, 17, 679205, tzinfo=utc), verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='data_termino',
            field=models.DateField(default=datetime.datetime(2022, 1, 31, 3, 31, 17, 679205, tzinfo=utc), verbose_name='Date de création'),
        ),
    ]
