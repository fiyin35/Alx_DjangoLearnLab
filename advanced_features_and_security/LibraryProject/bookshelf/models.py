from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(null=False)

    class Meta:
        permissions = [
            ('can_view', ' can view'),
            ('can_create', ' can create'),
            ('can_edit', ' can edit')
            ('can_delete', ' can delete')
        ]

    def __str__(self):
        return f"{self.title} by {self.author} published in {self.publication_year}"

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos', null=True, blank=True)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, phone_number, date_of_birth=None, profile_photo=None):
        if not email:
            raise ValueError("Please provide an email address")
        if not password:
            raise ValueError("Please provide a password")
        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, date_of_birth=date_of_birth, profile_photo=profile_photo)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, phone_number, date_of_birth=None, profile_photo=None):
        user = self.model(email, password, phone_number, date_of_birth, profile_photo)
        user.setDefault('is_staff', True)
        user.setDefault('is_superuser', True)

        if user.get('is_staff') is not True and user.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_staff and is_supervisor equal to true") 
        
        return self.create_user(email, password, phone_number, date_of_birth, profile_photo)

    

