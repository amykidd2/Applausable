# Generated by Django 2.2.3 on 2020-03-28 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0008_song_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='albumCover',
            field=models.ImageField(default='default_album.png', upload_to='C:\\Users\\euanw\\Workspace\\Applausable_WAD2_Group_Project\\mediaalbum_covers/'),
        ),
    ]
