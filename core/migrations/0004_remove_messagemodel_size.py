# Generated by Django 3.0.7 on 2021-04-21 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_messagemodel_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messagemodel',
            name='size',
        ),
    ]