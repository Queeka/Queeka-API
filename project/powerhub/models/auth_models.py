from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
import string, random
from django.db import models
from django.utils import timezone
from uuid import uuid4
from datetime import timedelta


class CustomUserManager(BaseUserManager):
    def create_user(self, contact, password=None, **extra_fields):
        if not contact:
            raise ValueError('The Contact field must be set')
        user = self.model(contact=contact, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, contact, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(contact, password, **extra_fields)


class User(AbstractUser):
    # User Information
    id = models.UUIDField(default=uuid4, primary_key=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)
    contact = models.CharField(max_length=15, unique=True)
    profile_image = models.ImageField(null=True)
    is_individual = models.BooleanField(default=False)
    # is_business = models.BooleanField(default=False)
    tier_1 = models.BooleanField(default=False)
    tier_2 = models.BooleanField(default=False)
    tier_3 = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'contact'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    def save(self, *args, **kwargs):
        if self.password:
            self.set_password(self.password)
        if not self.contact:
            random_digit = "".join(random.choices(string.digits, k=5))
            self.contact = random_digit
        if not self.username:
            random_username = "".join(random.choices(string.ascii_lowercase + string.digits, k=5))
            self.username=random_username
        super(User, self).save(*args, **kwargs)


#AdminQueeka10
# Define ConfirmationCode model
class ConfirmationCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    generated_confirmation_code = models.IntegerField(unique=True)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name
    
    def is_valid(self):
        return self.created_at >= timezone.now() - timedelta(minutes=10)

    @staticmethod
    def generate_confirmation_code():
        return ''.join(random.choices(string.digits, k=4))

    def save(self, *args, **kwargs):
        if not self.generated_confirmation_code:
            self.generated_confirmation_code = self.generate_confirmation_code()
        super().save(*args, **kwargs)



class QueekaBusiness(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, unique=True)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    business_sn = models.CharField(max_length=10, null=False)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.business_sn:
            serial_number = "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
            self.business_sn = serial_number
        super(QueekaBusiness, self).save(*args, **kwargs)
        
        
        
