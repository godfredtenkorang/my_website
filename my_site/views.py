from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from .utils import send_sms
from django.http import JsonResponse

def home(request):
    blogs = Blog.objects.all()[:3]
    category = request.GET.get('category')
    
    if category == None:
        portfolios = Portfolio.objects.order_by('image')
    else:
        portfolios = Portfolio.objects.filter(category__name=category)
    categories = Category.objects.all()
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
        
        send_mail(
            f"New Contact from {name}",
            f'Message:{message} \n {phone} \n {email} \n end',
                email,  # From email
                [settings.EMAIL_HOST_USER],  # To email
                fail_silently=False,
        ),
        
        return redirect('home')
    
    context = {
        'blogs': blogs,
        'categories': categories,
        'portfolios': portfolios,
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

def blog_detail(request, blog_slug):
    blog = Blog.objects.get(slug=blog_slug)
    
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


def sms(request):
    if request.method == 'POST':
        recipients = request.POST.get("recipients").split(",")
        recipients = [recipient.strip() for recipient in recipients]
        message = request.POST.get('message')
        response = send_sms(recipients, message)
        
        SMSLog.objects.create(
            recipients=", ".join(recipients),
            message=message, 
            status=response.get('status'), 
            response=response,
        )
        return JsonResponse(response)
    return render(request, 'my_site/send_sms.html')


def custom_404(request, exception):
    return render(request, 'my_site/404.html', status=404)