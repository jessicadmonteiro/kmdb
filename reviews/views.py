from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import PermissionReview
from .models import Review
from movies.models import Movie
from .serializers import ReviewSerializer
from django.shortcuts import get_object_or_404


class ReviewView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [PermissionReview]

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_url_kwarg = "movie_id"

    def perform_create(self, serializer):
        movie = get_object_or_404(Movie, id=self.kwargs["movie_id"])

        return serializer.save(critic=self.request.user, movie=movie)

    def get_queryset(self):
        movie = get_object_or_404(Movie, id=self.kwargs["movie_id"])

        return Review.objects.filter(movie=movie)
