from django.db import models

# Create your models here.

class User(models.Model):
    userId = models.IntegerField()
    userName = models.CharField(max_length = 100)
    passwordHash = models.CharField(max_length = 100)
    Name = models.CharField(max_length = 100)
    profileImage = models.ImageField()

class UserImage(models.Model):
    image = models.ImageField()
    User = models.ForeignKey(User, on_delete=models.CASCADE)