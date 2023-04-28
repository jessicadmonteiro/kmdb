from rest_framework import serializers
from .models import Movie
from genres.models import Genre
from genres.serializers import GenreSerializer


class MovieSerializer(serializers.ModelSerializer):

    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "duration",
            "premiere",
            "budget",
            "overview",
            "genres",
        ]

    def create(self, validated_data):

        genres_data = validated_data.pop("genres")

        create_movie = Movie.objects.create(**validated_data)

        for genre in genres_data:

            genres_obj = Genre.objects.filter(
                name__iexact=genre["name"]
            ).first()

            if not genres_obj:
                genres_obj = Genre.objects.create(**genre)

            create_movie.genres.add(genres_obj)

        return create_movie
