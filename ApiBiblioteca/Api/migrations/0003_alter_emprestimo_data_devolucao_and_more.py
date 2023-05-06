# Generated by Django 4.1.7 on 2023-05-05 19:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_alter_emprestimo_data_devolucao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_devolucao',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 4, 19, 50, 28, 708129, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='status',
            field=models.CharField(choices=[('emprestado', 'Emprestado'), ('atrasado', 'Atrasado'), ('devolvido', 'Devolvido')], default='emprestado', max_length=50),
        ),
    ]