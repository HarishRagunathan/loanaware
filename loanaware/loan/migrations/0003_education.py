# Generated by Django 5.0.3 on 2024-04-01 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0002_business_create_at_business_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('details', models.CharField(max_length=2000)),
                ('benifit', models.CharField(max_length=2000)),
                ('eligible', models.CharField(max_length=2000)),
                ('application', models.CharField(max_length=2000)),
                ('documents', models.CharField(max_length=2000)),
                ('status', models.BooleanField(default=False, help_text='0-Show,1-Hidden')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
