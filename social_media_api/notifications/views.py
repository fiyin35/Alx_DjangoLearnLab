from rest_framework import permissions
from rest_framework.generics import ListAPIView
from .models import Notification
from .serializers import NotificationSerializer

# Create your views here.

class NotificationListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')
