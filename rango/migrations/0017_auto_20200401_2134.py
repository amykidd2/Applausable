# Generated by Django 2.2.3 on 2020-04-01 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0016_auto_20200401_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='artistImage',
            field=models.ImageField(default='artist.jpg', upload_to='C:\\Users\\amyki\\Workspace\\Applausable\\media'),
        ),
    ]