from django.urls import path
from . import views


urlpatterns = [
    path('', views.donate, name='donate'),
    path('make_payment', views.make_payment, name='make-payment'),
    path('make_payment/<str:ref>/',views.verify_payment, name='verify-payment'),
]