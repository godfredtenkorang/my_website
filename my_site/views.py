from django.shortcuts import render
from .models import *

def home(request):
    services = Services.objects.all()
    blogs = Blog.objects.all()
    portfolios = Portfolio.objects.all()
    
    context = {
        'services': services,
        'blogs': blogs,
        'portfolios': portfolios
    }
    return render(request, "my_site/index.html", context)

def about(request):
    return render(request, 'my_site/about.html', {'title':'About'})


def resume(request):
    return render(request, 'my_site/resume.html', {'title': 'Resume'})

def blog(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
        'title': 'Blog',
    }
    return render(request, 'my_site/blog.html', context)

def blog_detail(request, pk):
    blog = Blog.objects.get(id=pk)
    
    context = {
        'blog':blog,
        'title': 'Blog Detail',
    }
    return render(request, 'my_site/blog_detail.html', context)
    

def portfolio(request):
    category = request.GET.get('category')
    
    if category == None:
        portfolios = Portfolio.objects.order_by('image')
    else:
        portfolios = Portfolio.objects.filter(category__name=category)
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'portfolios': portfolios,
        'title': 'Portfolio',
    }
    return render(request, 'my_site/portfolio.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
        return render(request, 'my_site/contact.html')
    return render(request, 'my_site/contact.html', {'title': 'Contact'},)
