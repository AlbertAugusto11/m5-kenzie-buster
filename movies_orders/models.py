from django.db import models


class MovieOrder(models.Model):
    purchased_at = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE
    )
    movies = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE
    )
