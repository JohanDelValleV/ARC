# Generated by Django 2.2.1 on 2019-07-02 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rfid', '0002_rfid_id_rfid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rfid',
            old_name='create',
            new_name='created',
        ),
    ]