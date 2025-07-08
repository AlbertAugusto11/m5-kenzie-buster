from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import UserSerializer


class UserViews(APIView):
    def post(self, request):
        serializer_data = UserSerializer(data=request.data)

        if serializer_data.is_valid():
            user = serializer_data.save()
            response_data = UserSerializer(user).data

            return Response(response_data, 201)
        else:
            return Response(serializer_data.errors, 400)
