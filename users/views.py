from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import CustomJWTSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class UserViews(APIView):
    def post(self, request):
        serializer_data = UserSerializer(data=request.data)

        if serializer_data.is_valid():
            user = serializer_data.save()
            response_data = UserSerializer(user).data

            return Response(response_data, 201)
        else:
            return Response(serializer_data.errors, 400)


class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer
