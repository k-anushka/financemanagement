from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(models.Model):
    ADMIN = 'admin'
    MEMBER = 'member'
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (MEMBER,'Member'),
    ]
    user_name=models.CharField(max_length=140)
    password=models.CharField(max_length=140)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=MEMBER)
    REQUIRED_FIELDS = ('user_name','password')
   
        
class Xpenses(models.Model):
    CATEGORY_CHOICES = [
        ('Health', 'Health'),
        ('Electronics', 'Electronics'),
        ('Travel', 'Travel'),
        ('Education', 'Education'),
        ('Books', 'Books'),
        ('Others', 'Others'),
    ]
    name = models.CharField(max_length=140)
    description = models.TextField()
    date = models.DateField()
    amount= models.PositiveBigIntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=20,default="admin")




