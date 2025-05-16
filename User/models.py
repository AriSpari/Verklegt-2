from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Custom User Manager to handle user creation
class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)  # hash the password before saving
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        """
        Create and return a superuser with a username and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)

# Custom User model
class User(AbstractBaseUser):
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)  # Make username unique
    name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='')

    email = models.EmailField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    is_seller = models.BooleanField(default=False)
    seller_bio = models.TextField(blank=True, null=True)

    # These fields are required by Django's User model
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Required for creating a superuser
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']  # Add other fields that you want to make required

    objects = CustomUserManager()

    def __str__(self):
        return self.username
