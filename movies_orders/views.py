from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from movies_orders.serializers import MovieOrderSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class MovieOrderViews(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, movie_id):
        serializer = MovieOrderSerializer(
            data=request.data,
            context={'request': request, 'movie_id': movie_id}
        )

        if serializer.is_valid():
            movier_order = serializer.save()

            return Response(MovieOrderSerializer(movier_order).data, 201)
        else:
            return Response(serializer.errors, 400)
