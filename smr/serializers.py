from django.forms import widgets
from rest_framework import serializers
from smr.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'director', 'popularity', 'genre', 'imdb_score')