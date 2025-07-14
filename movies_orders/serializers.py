from rest_framework import serializers

from movies.models import Movie
from movies_orders.models import MovieOrder


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    purchased_at = serializers.DateField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)

    purchased_by = serializers.EmailField(source='user.email', read_only=True)
    title = serializers.CharField(source='movie.title', read_only=True)

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user if request else None
        movie_id = self.context.get("movie_id")

        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            raise serializers.ValidationError("Filme não encontrado")

        order = MovieOrder.objects.create(
            user=user,
            movies=movie,
            price=validated_data['price']
        )
        return order
