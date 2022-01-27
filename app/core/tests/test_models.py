from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an emails is successful"""
        email = 'test@gbmsolucoesweb.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test the email for a new user is normalized"""
        email = 'test@GBMSOLUCOESWEB.COM'
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """
        Test if an error is raised if a user is createad with an invalid email
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_superuser(self):
        """Test crerating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@gbmsolucoesweb.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
    
    def test_article_str(self):
        """Test the article string representation"""
        article = models.Article.objects.create(
            title='New article'
        )
        self.assertEqual(str(article), article.title)

    def test_launch_str(self):
        """Test the launch string representation"""
        launch = models.Launch.objects.create(
            provider = 'Provider Name'
        )

        self.assertEqual(str(launch), launch.provider)
    
    def test_event_str(self):
        """Test the event string representation"""
        event = models.Event.objects.create(
            provider = 'Provider Name'
        )

        self.assertEqual(str(event), event.provider)
