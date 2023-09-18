from django.shortcuts import render
from . models import Product,Offer

# Create your views here.

from django.http import HttpResponse

def home(request):
    products=Product.objects.all()
    return render(request,'index.html',{'products':products})