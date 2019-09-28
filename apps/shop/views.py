from django.shortcuts import render
from apps.about.views import getinfo
from .models import *
# Create your views here.
def shop(request):
    product = Product.objects.all()
    context = {
        'info':getinfo(),
        'product':product
    }
    return render(request,'shop/shop.html',context)

def getproduct():
    return Product.objects.all()
    
def getsex():
    return Sex.objects.all()