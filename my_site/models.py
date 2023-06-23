from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField


class Services(models.Model):
    image = models.ImageField(upload_to="services-img", default="")
    title = models.CharField(max_length=50)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
class Article(models.Model):
    article = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.article
    
class Blog(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog-img', default='')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
        
class Portfolio(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio-img', default='')
    title = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    
    def __str__(self):
        return str(self.category)
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="post-img", default="")
    
    def __str__(self):
        return self.title
    
