from rest_framework import serializers
from movies.models import Movie, RatingChoices


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, required=False, default="")
    rating = serializers.ChoiceField(
        choices=RatingChoices,
        default=RatingChoices.GENERAL_AUDIENCES
        )
    synopsis = serializers.CharField(required=False, default="")
    added_by = serializers.EmailField(source='user.email', read_only=True)

    def create(self, validated_data):
        user = self.context['request'].user
        movie = Movie.objects.create(user=user, **validated_data)

        return movie
