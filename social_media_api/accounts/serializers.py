from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token   # <-- required import

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)   # <-- required

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "bio", "profile_picture")

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"],
        )
        user.bio = validated_data.get("bio", "")
        user.profile_picture = validated_data.get("profile_picture", None)
        user.save()

        # Generate token here
        Token.objects.create(user=user)   # <-- required

        return user
