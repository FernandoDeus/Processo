# Generated by Django 4.0.1 on 2022-01-31 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='valor_projeto',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
