from django.shortcuts import render
from .models import *
# Create your views here.
# Create your views here.
def about(request):
    info = About.objects.all()
    context = {
        'info':info
    }
    return render(request, 'about/about.html',context)

def getinfo():
    return About.objects.all()