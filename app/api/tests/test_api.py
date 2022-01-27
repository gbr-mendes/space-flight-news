from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from core import models, utils

ARTICLES_URL = reverse('api:retrive_articles')


class TestPublicAPIRequest(TestCase):
    """Tests for requests from unauthenticated users"""
    def setUp(self):
        self.client = APIClient()

        self.article_payload = {
            'title': 'New Article',
            'featured': True,
            'url': 'https://www.gbmsolucoesweb.com',
            'imageUrl': '',
            'newsSite': 'Some news',
            'summary': 'Some summary',
        }
    
    def retrive_articles_success(self):
        """Test retriving all the articles from db successfuly"""
        quantity = 2
        articles = utils.HelperTest.create_multiples_articles(quantity)
        res = self.client.get(ARTICLES_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), quantity)
        for article in articles:
            self.assertIn(str(article.id), res.data)
    
    def test_retrive_especific_article(self):
        """Test retrive article by id"""
        article = models.Article.objects.create(
            title='Article Title'
        )
        RETRIVE_ARTICLE_URL = reverse(
            'api:retrive_article',
            kwargs={'pk':article.id}
        )

        res = self.client.get(RETRIVE_ARTICLE_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['id'], str(article.id))
        
    def test_create_article(self):
        """Test adding an article to database"""

        res = self.client.post(ARTICLES_URL, self.article_payload)
        print(res.data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        id = res.data['id']
        exists = models.Article.objects.filter(id=id).exists()
        self.assertTrue(exists)
    
    def test_update_article(self):
        """Test update article - put method"""
        article = models.Article.objects.create(title='Title Article')
        RETRIVE_ARTICLE_URL = reverse(
            'api:retrive_article',
            kwargs={'pk':article.id}
        )
        res = self.client.put(RETRIVE_ARTICLE_URL, self.article_payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        article.refresh_from_db()
        self.assertEqual(res.data['url'], article.url)
        self.assertEqual(res.data['summary'], article.summary)
        self.assertEqual(res.data['newsSite'], article.newsSite)
    
    def test_delete_article(self):
        """Test delete an especific article"""
        article = models.Article.objects.create(title='Title Article')
        RETRIVE_ARTICLE_URL = reverse(
            'api:retrive_article',
            kwargs={'pk':article.id}
        )
        res = self.client.delete(RETRIVE_ARTICLE_URL, self.article_payload)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        id = article.id
        exists = models.Article.objects.filter(id=id).exists()
        self.assertFalse(exists)
