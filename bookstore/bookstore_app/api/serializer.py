from rest_framework import serializers
from django.utils import timezone

class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    def validate(self, data):
        return data

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    author = serializers.CharField(max_length=200)

    def validate(self, data):
        return data

class UpdateBookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    new_title = serializers.CharField(max_length=200)

    def validate(self, data):
        return data
