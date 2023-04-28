import uuid
from django.db import models


class Genre(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=127)
    movies = models.ManyToManyField("movies.Movie", related_name="genres")
