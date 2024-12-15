from django.shortcuts import get_object_or_404
from rest_framework.response import Response 
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import permissions, status
from .models import CustomUser
from .serializers import UserSerializer, LoginSerializer, RegistrationSerializer


# Create your views here.
class RegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegistrationSerializer


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

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
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer


class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        follow_user = get_object_or_404(CustomUser, id=user_id)

        if request.user == follow_user:
            return Response({'detail': 'You can not follow yourself'}, status=status.HTTP_400_BAD_REQUEST)
        
        request.user.following.add(follow_user)
        return Response({'detail': f'You are now following {follow_user.username}'}, status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        unfollow_user = get_object_or_404(CustomUser, id=user_id)

        if request.user == unfollow_user:
            return Response({'detail': 'You can unfollow yourself'}, status=status.HTTP_400_BAD_REQUEST)
        
        request.user.following.remove(unfollow_user)
        return Response({'detail': f'You have unfollowed {unfollow_user.username}'}, status=status.HTTP_200_OK)

