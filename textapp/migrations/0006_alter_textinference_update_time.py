# Generated by Django 5.1.4 on 2025-02-03 03:09

import textapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textapp', '0005_alter_textinference_update_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textinference',
            name='update_time',
            field=models.DateTimeField(default=textapp.models.get_taipei_time),
        ),
    ]
