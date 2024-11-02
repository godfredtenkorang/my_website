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
    content = models.TextField(null=True, blank=True, default="")
    content1 = models.TextField(null=True, blank=True, default="")
    content2 = models.TextField(null=True, blank=True, default="")
    content3 = models.TextField(null=True, blank=True, default="")
    content4 = models.TextField(null=True, blank=True, default="")
    content5 = models.TextField(null=True, blank=True, default="")
    content6 = models.TextField(null=True, blank=True, default="")
    content7 = models.TextField(null=True, blank=True, default="")
    content8 = models.TextField(null=True, blank=True, default="")
    content9 = models.TextField(null=True, blank=True, default="")
    content10 = models.TextField(null=True, blank=True, default="")
    content11 = models.TextField(null=True, blank=True, default="")
    content12 = models.TextField(null=True, blank=True, default="")
    content13 = models.TextField(null=True, blank=True, default="")
    content14 = models.TextField(null=True, blank=True, default="")
    content15 = models.TextField(null=True, blank=True, default="")
    content16 = models.TextField(null=True, blank=True, default="")
    content17 = models.TextField(null=True, blank=True, default="")
    content18 = models.TextField(null=True, blank=True, default="")
    content19 = models.TextField(null=True, blank=True, default="")
    content20 = models.TextField(null=True, blank=True, default="")
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
    
    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.name