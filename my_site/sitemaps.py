from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Portfolio, Category

class StaticSitemap(Sitemap):
    def items(self):
        return ['home','portfolio']
    
    def location(self, item):
        return reverse(item)
    
class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()
    
class PortFolioSitemap(Sitemap):
    def items(self):
        return Portfolio.objects.all()[:100]