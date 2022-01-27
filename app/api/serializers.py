from fileinput import filename
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
    launches = LaunchSerializer(many=True)
    events = EventSerializer(many=True)
    class Meta:
        model = models.Article
        fields = (
            'id', 'featured', 'title', 'url', 'imageUrl', 'newsSite',
            'summary', 'publishedAt', 'launches', 'events'
        )

    def create(self, validated_data):
        launches_data = validated_data.pop('launches', None)
        events_data = validated_data.pop('events', None)
        article = models.Article.objects.create(**validated_data)
        
        if launches_data:
            list_launch = []
            for launch in launches_data:
                new_launch = models.Launch.objects.create(**dict(launch))
                list_launch.append(new_launch)
            article.launches.set(list_launch)
            article.save()

        if events_data:
            list_event = []
            for event in events_data:
                new_event = models.Event.objects.create(**dict(event))
                list_event.append(new_event)
            article.events.set(list_event)
            article.save()
        
        return article

    def update(self, instance, validated_data):
        launches_data = validated_data.pop('launches', None)
        events_data = validated_data.pop('events', None)
        models.Article.objects.filter(id=instance.id).update(
            **validated_data
        )

        instance = models.Article.objects.get(id=instance.id)

        if launches_data:
            list_launch = []
            for launch in launches_data:
                new_launch = models.Launch.objects.create(**dict(launch))
                list_launch.append(new_launch)
            instance.launches.set(list_launch)
            instance.save()
        
        if events_data:
            list_event = []
            for event in events_data:
                new_event = models.Event.objects.create(**dict(event))
                list_event.append(new_event)
            instance.events.set(list_event)
            instance.save()
        return instance