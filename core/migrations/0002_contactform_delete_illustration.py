# Generated by Django 4.0.1 on 2022-01-26 21:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField()),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Illustration',
        ),
    ]