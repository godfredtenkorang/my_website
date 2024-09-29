from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_view),
    path('blog/<int:id>/', views.get_blog),
]