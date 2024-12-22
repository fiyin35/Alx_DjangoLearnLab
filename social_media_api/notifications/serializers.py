from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.Serializer):
    target = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'target', 'timestamp']

    def get_target(self, obj):
        return str(obj.target)  # Convert the target object to a string