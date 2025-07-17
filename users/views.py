from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from users.permissions import IsUserOwner
from users.serializers import CustomJWTSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class UserViews(APIView):
    def post(self, request):
        serializer_data = UserSerializer(data=request.data)

        if serializer_data.is_valid():
            user = serializer_data.save()
            response_data = UserSerializer(user).data

            return Response(response_data, 201)
        else:
            return Response(serializer_data.errors, 400)


class UserDetailViews(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsUserOwner]

    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)

        self.check_object_permissions(request, user)

        serializer = UserSerializer(user)
        return Response(serializer.data, 200)

    def patch(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(request, user)

        serializer_request = UserSerializer(user, request.data, partial=True)
        if serializer_request.is_valid():
            serializer = serializer_request.save()
            return Response(UserSerializer(serializer).data, 200)

        else:
            return Response(serializer_request.errors, 400)


class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer
