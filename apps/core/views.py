from django.shortcuts import render
from apps.about.views import getinfo
from apps.blog.views import getdatablog
from apps.shop.views import getproduct, getsex
from apps.shop.models import *
# Create your views here.
def home(request):
    info = getinfo()
    blog = getdatablog()
    product = getproduct()   
    sex = getsex()

    cat = Category.objects.all()

    context = {
        'info':info,
        'blog':blog,
        'sex':sex,
        'product':product
    }
    return render(request, 'core/home.html',context)
