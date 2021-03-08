from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.


def send_mail_to(request):
    send_mail("Hi!", "This my first mes","Hermes",["bulnikn@gmail.com",])
    return HttpResponse("<p>I send mail<p>")