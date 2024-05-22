from rest_framework import viewsets
from user_profile.models import UserProfile
from . import serializers

class UserViewset(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer