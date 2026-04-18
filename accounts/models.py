from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    language = models.CharField(
        max_length=20,
        choices=[
            ('en','English'),
            ('ta','Tamil'),
            ('hi','Hindi'),
            ('te','Telugu'),
            ('kn','Kannada'),
            ('ml','Malayalam')
        ],
        default='en'
    )