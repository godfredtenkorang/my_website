from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    services = Services.objects.all()
    blogs = Blog.objects.all()
    portfolios = Portfolio.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
        return render(request, 'my_site/index.html')
    context = {
        'services': services,
        'blogs': blogs,
        'portfolios': portfolios
    }
    return render(request, "my_site/index.html", context)

def about(request):
    return render(request, 'my_site/about.html')


def resume(request):
    return render(request, 'my_site/resume.html')

def blog(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'my_site/blog.html', context)

def portfolio(request):
    portfolios = Portfolio.objects.all()
    context = {
        'portfolios': portfolios
    }
    return render(request, 'my_site/portfolio.html', context)

def youtube(request):
    youtube = Youtube.objects.all()
    posts = Post.objects.all()
    context = {
        'youtubes':youtube,
        'posts':posts
    }
    return render(request, "my_site/youtube.html", context)

def contact(request):
    
    return render(request, 'my_site/contact.html')