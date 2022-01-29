from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api import serializers

from core import models


class ExibitionView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        return Response('Back-end Challenge 2022 -🏅- Space Flight News')


class ArticlesAPIView(generics.ListCreateAPIView):
    """Views to articles endpoint"""
    serializer_class = serializers.ArticleSerializer
    permission_classes = (AllowAny,)
    queryset = models.Article.objects.all().order_by('-publishedAt')
    


class ArticleAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Views to retrive an especific article endpoint"""
    serializer_class = serializers.ArticleSerializer
    permission_classes = (AllowAny,)
    queryset = models.Article.objects.all()