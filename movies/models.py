import uuid
from django.db import models


class Movie(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=127)
    duration = models.DurationField(max_length=150)
    premiere = models.DateField()
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    overview = models.TextField(default=None, null=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="movies")
