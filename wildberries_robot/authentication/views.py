from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from authentication.models import User
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from authentication.serializers import RegisterSerializer, LoginSerializer


class RegisterGenericAPIView(generics.GenericAPIView):
    """Registration for users"""
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        return Response(user_data, status=status.HTTP_201_CREATED)


class LoginGenericAPIView(generics.GenericAPIView):
    """Login for users"""
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user = get_object_or_404(User, email=request.data['email'])
        token = str(RefreshToken.for_user(user).access_token)
        return Response({'token': token}, status=status.HTTP_200_OK)


class LogoutGenericAPIView(generics.GenericAPIView):
    """Logout for users"""

    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
