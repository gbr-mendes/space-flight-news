from rest_framework import generics
from rest_framework.permissions import AllowAny

from api import serializers

from core import models


class ArticlesAPIView(generics.ListCreateAPIView):
    """Views to articles endpoint"""
    serializer_class = serializers.ArticleSerializer
    permission_classes = (AllowAny,)
    queryset = models.Article.objects.all()


class ArticleAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Views to retrive an especific article endpoint"""
    serializer_class = serializers.ArticleSerializer
    permission_classes = (AllowAny,)
    queryset = models.Article.objects.all()
