import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                                        PermissionsMixin
from django.utils import timezone

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new supersuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that suports using email instead username"""
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Article(models.Model):
    """Model for article table on database"""
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    featured = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True)
    imageUrl = models.ImageField(blank=True, upload_to='images/%Y/%m', null=True)
    newsSite = models.CharField(max_length=255, blank=True)
    summary = models.CharField(max_length=255, blank=True)
    publishedAt = models.DateTimeField(default=timezone.now)
    launches = models.ManyToManyField('Launch')
    events = models.ManyToManyField('Event')

    def __str__(self):
        return self.title


class Launch(models.Model):
    """Model for Lauch table on database"""
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    provider = models.CharField(max_length=255)

    def __str__(self):
        return self.provider


class Event(models.Model):
    """Model for Event table on database"""
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    provider = models.CharField(max_length=255)

    def __str__(self):
        return self.provider