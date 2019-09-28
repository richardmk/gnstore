from django.shortcuts import render
from .models import *
from apps.shop.models import Product
from apps.about.views import getinfo
# Create your views here.
def blog(request):
    post = Post.objects.filter(state=True)
    category = Category.objects.all()
    pro = Product.objects.all()
    
    context = {
        'post':post,
        'category':category,
        'info':getinfo(),
        'pro':pro
    }
   
    return render(request, 'blog/blog.html',context)

def detail_post(request,slug):

    d_post = Post.objects.get(slug=slug)
    category = Category.objects.all()
    pro = Product.objects.all()
    
    context = {
        'd_post':d_post,
        'category':category,
        'pro':pro
        
    }

    return render(request, 'blog/detail_post.html',context)

def getdatablog():
    return Post.objects.all()    