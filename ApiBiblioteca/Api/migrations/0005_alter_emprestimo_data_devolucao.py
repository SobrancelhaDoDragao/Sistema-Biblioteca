# Generated by Django 4.1.7 on 2023-05-05 19:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0004_alter_emprestimo_data_devolucao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_devolucao',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 4, 19, 51, 9, 588738, tzinfo=datetime.timezone.utc)),
        ),
    ]