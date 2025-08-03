from rest_framework import serializers
from .models import Author, Book, Publisher

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_days_since_created(self, obj):
        return (date.today() - obj.created_at.date()).days

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'