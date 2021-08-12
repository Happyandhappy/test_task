from rest_framework import serializers
from .models import Tweet


class TweetSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, required=True)
    message = serializers.CharField(max_length=50, required=False)
    create_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)

    def create(self, validated_data):
        return Tweet.objects.create(**validated_data)
