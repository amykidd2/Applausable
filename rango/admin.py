from django.contrib import admin
from rango.models import UserProfile, Artist, Album, Song, Review

admin.site.register(UserProfile) 

#Apparently can't display the forgien key 'artistID'
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('albumID', 'albumName','slug')
admin.site.register(Album, AlbumAdmin)

class SongAdmin(admin.ModelAdmin):
    list_display = ('songID', 'title', 'slug', 'overallScore', 'genre')
admin.site.register(Song, SongAdmin)

class ArtistAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('artistName',)}
    list_display = ('artistID', 'artistName', 'genre', 'description', 'LinkToSocialMedia', 'slug')
admin.site.register(Artist, ArtistAdmin)

admin.site.register(Review)
