from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField

# Create your models here.
class Services(models.Model):
    image = models.ImageField(upload_to="services-img", default="")
    title = models.CharField(max_length=50)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog-img', default='')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.URLField(max_length=200)
    
    def __str__(self):
        return self.title
    
class Youtube(models.Model):
    title = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-added"]
        
class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio-img', default='')
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    
    def __str__(self):
        return self.title
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="post-img", default="")
    
    def __str__(self):
        return self.title
    