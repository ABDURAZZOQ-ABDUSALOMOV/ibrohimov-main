from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser):
    img = models.ImageField(upload_to='profile-img/', default='default_user.png')
    phone = models.CharField(max_length=20)
    





