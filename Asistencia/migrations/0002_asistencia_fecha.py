# Generated by Django 2.2.1 on 2019-07-03 11:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencia',
            name='fecha',
            field=models.DateTimeField(default=datetime.date(2019, 7, 3)),
        ),
    ]
