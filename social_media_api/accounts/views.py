from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import CustomUser
from .serializers import UserSerializer, LoginSerializer, RegistrationSerializer


# Create your views here.
class RegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        """This method tries to fetch the 
        Token associated with the specified user. 
        If it does not exist, it creates a new 
        Token for the user"""
        token, created = Token.objects.get_or_create(user=user)

        return Response({'token': token.key, 'user': UserSerializer(user).data, 'created': created})
    
class ProfileView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    

