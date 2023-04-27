from rest_framework import permissions, serializers
from django.contrib.auth.models import User
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email"]

class EventSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    moderator = UserSerializer(read_only=True)
    attendees = UserSerializer(read_only=True)

    class Meta:
        model = models.Event
        fields = "__all__"
