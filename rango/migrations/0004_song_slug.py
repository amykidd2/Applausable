# Generated by Django 2.2.3 on 2020-03-17 19:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_album_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, unique=True),
        ),
    ]
