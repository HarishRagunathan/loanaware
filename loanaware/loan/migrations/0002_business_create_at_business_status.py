# Generated by Django 5.0.3 on 2024-04-01 03:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='business',
            name='status',
            field=models.BooleanField(default=False, help_text='0-Show,1-Hidden'),
        ),
    ]
