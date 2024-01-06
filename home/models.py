from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Home (models.Model):
    name = models.CharField(max_length=20)
    job = models.CharField(max_length=50)
    image = models.ImageField(upload_to='home/', null=True,blank=True)

    def __str__(self):
        return self.name


class About (models.Model):
    name =models.CharField(max_length=20)
    profile = models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    phone = models.IntegerField(blank=True, help_text='Contact phone number')
    image = models.ImageField(upload_to='about/')
    aboutme = models.TextField(max_length=20000)

    def __str__(self):
        return self.name

class Skill (models.Model):
    skill = models.CharField(max_length=15)
    percentage = models.IntegerField()
    def __str__(self):
        return self.skill


class Service (models.Model):
    title = models.CharField(max_length=200)
    icon1 = models.CharField(max_length=20)
    icon2 = models.CharField(max_length=20)
    job = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=500)
    def __str__(self):
        return self.job


class Portfoilo(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='protfolio/')
    text = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    date = models.DateField(default=1, null =True,blank=True)
    def __str__(self):
        return self.title      

class Blog (models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog/')
    cattigory = models.ForeignKey('Cattigory', related_name = 'blog_cattigory', on_delete = models.CASCADE)
    text = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=500)
    author = models.ForeignKey(User, related_name ='blog_author', on_delete = models.CASCADE)
    auth_image = models.ImageField(upload_to='auth/')
    def __str__(self):
        return self.title



class Cattigory (models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name