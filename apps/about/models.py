from django.db import models
from apps.core.models import BaseModel

# Create your models here.

class About(BaseModel):
    story =  models.TextField('Story')
    mision = models.TextField('Mision')
    email = models.EmailField('Email', max_length=254)
    address =  models.CharField('Address', max_length=50)
    phone = models.CharField('Phone', max_length=50)
    facebook = models.URLField('Facebook', max_length=200)
    twitter = models.URLField('Twitter', max_length=200)
    instagram = models.URLField('Instagram', max_length=200)
    youtube = models.URLField('Youtube', max_length=200)
    github = models.URLField('Github', max_length=200)

    class Meta:
        verbose_name = "About"

    def __str__(self):
        return self.story    
