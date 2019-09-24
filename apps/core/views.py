from django.shortcuts import render
from apps.about.views import getinfo
# Create your views here.
def home(request):
    contexto = {
        'info':getinfo()
    }
    return render(request, 'core/home.html',contexto)
