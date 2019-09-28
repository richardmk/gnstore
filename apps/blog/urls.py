from django.urls import path
from .views import * #otra manera de llamar a las rutas

urlpatterns = [
    path('', blog, name = 'blog'),
    path('<slug:slug>/', detail_post, name = 'detail_post'),
]
