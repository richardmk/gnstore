from django.shortcuts import render
from apps.about.views import getinfo
from .models import *
# Create your views here.
def shop(request):
    product = Product.objects.all()
    category = Category.objects.all()
    context = {
        'info':getinfo(),
        'product':product,
        'category':category
    }
    return render(request,'shop/shop.html',context)

def getproduct():
    return Product.objects.all()

def getsex():
    return Sex.objects.all()

def get_product_prom():
    return Product.objects.filter(promotion=True)[:3]#indica solo los 3 primeros elementos de la lista
