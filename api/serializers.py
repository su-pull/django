from rest_framework import serializers
from .models import Docs, Talk
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class DocsSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Docs
        fields = ('id', 'title_ja', 'content_ja', 'description_ja', 'title_en', 'content_en', 'description_en', 'slug', 'created_at')


class TalkSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Talk
        fields = ('id', 'title_ja', 'content_ja', 'description_ja', 'title_en', 'content_en', 'description_en', 'slug', 'created_at')
