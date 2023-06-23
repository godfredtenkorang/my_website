from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('resume/', views.resume, name="resume"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('blog/', views.blog, name="blog"),
    path('<pk>/blog_detail/', views.blog_detail, name="blog_detail"),
    path("contact/", views.contact, name="contact"),
]