from django.shortcuts import render
from .models import *
from apps.shop.models import Product
from apps.about.views import getinfo
from apps.shop.views import get_product_prom
from django.db.models import Q



    
def blog(request):
    queryset = request.GET.get("search")

    post = Post.objects.filter(state=True)
    category = Category.objects.all()
    pro = Product.objects.all()
    
    if queryset:
        post = Post.objects.filter(
            Q(title__icontains=queryset) | #realizar busqueda como like %%
            Q(description__icontains=queryset) |
            Q(author__name__icontains=queryset) | #agregar el nombre del campo si es llave foranea
            Q(category__name__icontains=queryset) 
        ).distinct()

    context = {
        'post':post,
        'category':category,
        'info':getinfo(),
        'pro':pro,
        'get_product_prom':get_product_prom()
    }
   
    return render(request, 'blog/blog.html',context)






def detail_post(request,slug):
    queryset = request.GET.get("search")
    post = Post.objects.filter(state=True)
    d_post = Post.objects.get(slug=slug)
    category = Category.objects.all()
    pro = Product.objects.all()
     
    if queryset:
        post = Post.objects.filter(
            Q(title__icontains=queryset) | #realizar busqueda como like %%
            Q(description__icontains=queryset) |
            Q(author__name__icontains=queryset) | #agregar el nombre del campo si es llave foranea
            Q(category__name__icontains=queryset) 
        ).distinct()
        context = {
            'post':post,
            'category':category,
            'pro':pro,
            'get_product_prom':get_product_prom()
        }
        return render(request,'blog/blog.html',context)
    
    context = {
        'd_post':d_post,
        'category':category,
        'pro':pro,
        'get_product_prom':get_product_prom()
    }
    return render(request, 'blog/detail_post.html',context)

def getdatablog():
    return Post.objects.all()   

