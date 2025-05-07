from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.IntegerField()  # Changed userId to user_id
    username = models.CharField(max_length=100)  # Changed userName to user_name
    password = models.CharField(max_length=100)  # Changed passwordHash to password_hash
    name = models.CharField(max_length=100)  # Changed Name to name
    profile_image = models.ImageField(upload_to='')  # Changed profileImage to profile_image



class UserImage(models.Model):
    image = models.ImageField()
    User = models.ForeignKey(User, on_delete=models.CASCADE)