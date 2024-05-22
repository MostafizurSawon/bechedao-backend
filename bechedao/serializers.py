from rest_framework import serializers
from django.contrib.auth.models import User
from user_profile.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
