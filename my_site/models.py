from django.db import models
from django.utils import timezone
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f"/category/{self.id}/"

class Portfolio(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio-img', default='')
    title = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    
    class Meta:
        ordering = ['-title']

    def __str__(self):
        return str(self.category) 
    
    def get_absolute_url(self):
        return f"/porfolio /{self.id}/"


class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog-img', default='')
    content1 = models.TextField(null=True, default="", blank=True)
    content2 = models.TextField(null=True, default="", blank=True)
    content3 = models.TextField(null=True, default="", blank=True)
    content4 = models.TextField(null=True, default="", blank=True)
    content5 = models.TextField(null=True, default="", blank=True)
    content6 = models.TextField(null=True, default="", blank=True)
    content7 = models.TextField(null=True, default="", blank=True)
    content8 = models.TextField(null=True, default="", blank=True)
    content9 = models.TextField(null=True, default="", blank=True)
    content10 = models.TextField(null=True, default="", blank=True)
    content11 = models.TextField(null=True, default="", blank=True)
    content12 = models.TextField(null=True, default="", blank=True)
    content13 = models.TextField(null=True, default="", blank=True)
    content14 = models.TextField(null=True, default="", blank=True)
    content16 = models.TextField(null=True, default="", blank=True)
    content17 = models.TextField(null=True, default="", blank=True)
    content18 = models.TextField(null=True, default="", blank=True)
    content19 = models.TextField(null=True, default="", blank=True)
    content20 = models.TextField(null=True, default="", blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-date_posted',]
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        output_size = (300, 300)
        img.thumbnail(output_size)
        img.save(self.image.path)
        
    def get_image(self):
        if self.image:
            return f"https://godeytech.com" + self.image.url
        return ''
    
    def get_article(self):
        return self.content1
    
    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.name