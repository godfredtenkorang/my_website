from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('resume/', views.resume, name="resume"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('blog/', views.blog, name="blog"),
    path("youtube_channel/", views.youtube, name="youtube"),
    path("contact/", views.contact, name="contact"),
]