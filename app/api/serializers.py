from rest_framework import serializers

from core import models


class EventSerializer(serializers.ModelSerializer):
    """Serializers for event data"""
    class Meta:
        model = models.Event
        fields = ('id', 'provider')


class LaunchSerializer(serializers.ModelSerializer):
    """Serializers for Launch data"""
    class Meta:
        model = models.Launch
        fields = ('id', 'provider')


class ArticleSerializer(serializers.ModelSerializer):
    """Serialier for Article data"""
    class Meta:
        model = models.Article
        fields = (
            'id', 'featured', 'title', 'url', 'imageUrl', 'newsSite',
            'summary', 'publishedAt'
        )
