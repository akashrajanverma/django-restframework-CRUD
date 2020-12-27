from rest_framework import serializers
from django.utils import timezone

class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    added_by = serializers.CharField(max_length=200)
    created_date = serializers.DateTimeField(default=timezone.now)

    def validate_name(self, value):
        name = ['akash', 'vikas']
        if value.lower() not in name:
            raise serializers.ValidationError("Not a valid name")
        return value

    def validate_added_by(self, value):
        name = ['akash', 'mohit']
        if value.lower() not in name:
            raise serializers.ValidationError("Not a valid name")
        return value