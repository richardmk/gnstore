from django.urls import path
from .views import *

urlpatterns = [
    path('', Contact.as_view(), name = 'contact'),
    #path('detail/', views.blog_detail, name = 'blog_detail'),
]
