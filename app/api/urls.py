from django.urls import path
from api import views


app_name = 'api'

urlpatterns = [
    path('articles/', views.ArticlesAPIView.as_view(), name='retrive_articles'),
    path('articles/<uuid:pk>', views.ArticleAPIView.as_view(), name='retrive_article')
]
