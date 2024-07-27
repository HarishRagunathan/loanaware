# Generated by Django 5.0.3 on 2024-04-05 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0007_business_amount_business_interest_education_amount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='others',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('details', models.CharField(max_length=2000)),
                ('interest', models.IntegerField(default=0)),
                ('amount', models.FloatField(default=1)),
                ('benifit', models.CharField(max_length=2000)),
                ('eligible', models.CharField(max_length=2000)),
                ('application', models.CharField(max_length=2000)),
                ('documents', models.CharField(max_length=2000)),
                ('status', models.BooleanField(default=False, help_text='0-Show,1-Hidden')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='loan',
            name='category',
            field=models.CharField(default='-', max_length=100),
        ),
    ]
