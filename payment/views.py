from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import Payment
from django.conf import settings
from django.http import HttpRequest
from django.contrib import messages
from . import forms

# Create your views here.
def donate(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        payment_form = forms.PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            return render(request, 'payment/make_payment.html', {'payment':payment, 'paystack_public_key':settings.PAYSTACK_PUBLIC_KEY})
    else:
        payment_form = forms.PaymentForm()
    context = {
        'title': 'Donate',
        'payment_form':payment_form
    }
    return render(request, 'payment/donate.html', context)


def make_payment(request):
    return render(request, 'payment/make_payment.html')


def verify_payment(request: HttpRequest, ref:str) -> HttpResponse:
    payment = get_object_or_404(Payment, ref=ref)
    verified = payment.verify_payment()
    if verified:
        messages.success(request, "Payment succussful")
    else:
        messages.error(request, "Payment unsuccussful")
    return redirect('donate')