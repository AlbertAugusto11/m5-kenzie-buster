from movies.models import Movie
from movies.serializers import MovieSerializer
from .permissions import MyCustomPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response


class MovieViews(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermission]

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True, context={'request': request})

        return Response(serializer.data, 200)

    def post(self, request):
        movie_serializer = MovieSerializer(
            data=request.data,
            context={'request': request}
        )

        if movie_serializer.is_valid():
            movie = movie_serializer.save()

            return Response(MovieSerializer(movie).data, 201)
        else:
            return Response(movie_serializer.errors)


class MovieDetailsViews(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermission]

    def get(self, request, movie_id):
        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response({"detail": "Not found"}, 404)

        serializer = MovieSerializer(movie, context={'request': request})
        return Response(serializer.data, 200)

    def delete(self, request, movie_id):
        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response({"detail": "Not found"}, 404)

        movie.delete()
        return Response({}, 204)
