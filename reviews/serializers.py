
from rest_framework import serializers
from .models import Review
from users.models import User


class ReviewUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
        ]


class ReviewSerializer(serializers.ModelSerializer):

    movie_id = serializers.CharField(source="movie.id", read_only=True)
    critic = ReviewUserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = [
            "id",
            "stars",
            "review",
            "spoilers",
            "movie_id",
            "critic",
        ]

    def create(self, validated_data):
        return Review.objects.create(**validated_data)
