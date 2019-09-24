from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name = 'about'),
    #path('detail/', views.blog_detail, name = 'blog_detail'),
]
