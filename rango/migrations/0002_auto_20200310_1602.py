# Generated by Django 2.2.3 on 2020-03-10 16:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, unique=True),
        ),
    ]