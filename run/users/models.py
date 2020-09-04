from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from time import timezone
# Create your models here

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50,blank=False,unique=True)
    email = models.EmailField(max_length=50,unique=True,blank=False)
    password = models.CharField(max_length=100,blank=False)
    mobile_no = models.CharField(max_length=20,blank=True)
    city = models.CharField(max_length=50,blank=True)
    sports_category = models.CharField(max_length=50,blank=False)
    area = models.CharField(max_length=50,blank=True)
    profile_pic = models.ImageField(upload_to=None,blank=True)

    objects = CustomUserManager()
    # USERNAME_FIELD = name

    def __str__(self):
        return self.username
    

class Team(models.Model):
    team_name = models.CharField(max_length=20)
    players = models.ManyToManyField(CustomUser)
    capton = models.CharField(max_length=20)
    team_logo = models.ImageField(upload_to=None)
    area = models.CharField(max_length=30)
    sports = models.CharField(max_length=20)
    chalenges = models.CharField(max_length=20)
    def __str__(self):
        return self.team_name

class Challenge(models.Model):
    team1 = models.CharField(max_length=20)
    team2 = models.CharField(max_length=20)
    date_challenge = models.DateField(auto_now=True)
    status = models.CharField(max_length=20)
    date_match = models.DateTimeField()
    venue = models.CharField(max_length=20)
    average_age_group = models.CharField(max_length=20)

    def __str__(self):
        return self.team1,team2

class Sports(models.Model):
    sports_logo = models.ImageField(upload_to=None)
    names_list = models.CharField(max_length=20)

    def __str__(self):
        return self.names_list