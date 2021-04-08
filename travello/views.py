from django.shortcuts import render, redirect
from .models import Destination
from .models import Phone_Number
from .models import NewsLater
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
def index(request):
    dests = Destination.objects.all()
    phone = Phone_Number.objects.all()
    nsl = NewsLater.objects.all()
    
    # dest1 = Destination()
    # dest1.name = 'Rangpur'
    # dest1.des = "Very clean and place of peace. It's call the secoend Capital of North Bengal"
    # dest1.img = 'rangpur.jpg'
    # dest1.price = 800
    # dest1.offer = False

    # dest2 = Destination()
    # dest2.name = 'Pabna'
    # dest2.des = "Pabna district is famous for production of milk and various type of fruits"
    # dest2.img = 'pabna.jpg'
    # dest2.price = 500
    # dest2.offer = False

    # dest3 = Destination()
    # dest3.name = 'Panchagarh'
    # dest3.des = "Panchagarh is a district of the Rangpur division in Northern Bangladesh"
    # dest3.img = 'panchagarh.jpg'
    # dest3.price = 900
    # dest3.offer = True

    # # dest4 = Destination()
    # # dest4.name = 'Panchagarh'
    # # dest4.des = "Panchagarh is a district of the Rangpur division in Northern Bangladesh"
    # # dest4.img = 'panchagarh.jpg'
    # # dest4.price = 800

    # head = Navbar()
    # head.phone = "  01765967395"
    # head.call = "Call Us "


    # dests = [dest1,dest2,dest3]
    return render(request,"index.html",{'dests':dests,'phone':phone,'nsl':nsl})
    