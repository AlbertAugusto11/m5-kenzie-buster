from django.db import models


class RatingChoices(models.TextChoices):
    GENERAL_AUDIENCES = "G"
    PARENTAL_GUIDANCE = "PG"
    PARENTAL_STRONGLY = "PG-13"
    RESTRICTED = "R"
    ADULTS_ONLY = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, blank=True, default="")
    rating = models.CharField(
        max_length=20,
        choices=RatingChoices,
        default=RatingChoices.GENERAL_AUDIENCES
        )
    synopsis = models.CharField(blank=True, default="")

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies"
    )
    users = models.ManyToManyField(
        "users.User",
        through="movies_orders.MovieOrder",
        related_name="ordered_movies"
    )
