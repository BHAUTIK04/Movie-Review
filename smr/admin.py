from django.contrib import admin
from .models import Movie
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
	list_display = ['name','director','popularity','genre','imdb_score']
	search_fields = ['name','director']
	list_filter = ['imdb_score']
admin.site.register(Movie, MovieAdmin)

