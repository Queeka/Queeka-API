from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
import string, random
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
    # Create a standard user
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

def create_superuser(self, email, password=None, **extra_fields):
    # Create a superuser
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)

    if extra_fields.get('is_staff') is not True:
        raise ValueError('Superuser must have is_staff=True.')
    if extra_fields.get('is_superuser') is not True:
        raise ValueError('Superuser must have is_superuser=True.')

    return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    # User Information
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)
    contact = models.CharField(max_length=15, unique=True)
    
    USERNAME_FIELD = 'contact'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    def save(self, *args, **kwargs):
        if self.password:
            self.set_password(self.password)
        super().save(*args, **kwargs)


class Business(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, unique=True)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name