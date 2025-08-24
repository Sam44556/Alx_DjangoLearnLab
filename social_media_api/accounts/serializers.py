from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import Post, Comment
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    # Explicit password field (required by test)
    password = serializers.CharField(write_only=True)
   
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

        # Generate token on registration
        Token.objects.create(user=user)

        return user



class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "post", "author", "author_name", "content", "created_at"]


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.username", read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "content", "author", "author_name", "created_at", "updated_at", "comments"]
