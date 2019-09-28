from django.db import models
from apps.core.models import BaseModel
from ckeditor.fields import RichTextField
# Create your models here.

class Category(BaseModel):
    name = models.CharField('Category', max_length=100, unique= True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Author(BaseModel):
    name = models.CharField('Name', max_length=150)        
    email =  models.EmailField('Email', max_length=150)
    facebook = models.URLField('Facebook', max_length=150)
    instagram = models.URLField('Instagram', max_length=150)
   
    class Meta:
        verbose_name = 'Author'
        #verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name

class Post(BaseModel):
    title = models.CharField('title', max_length=150,blank=False,null=False)
    slug = models.CharField('Slug', max_length=100,blank=False,null=False)
    description = models.CharField('Description', max_length=250,blank=False,null=False)
    content = RichTextField('Content')
    imagen = models.URLField('Imagen', max_length=300,blank=False,null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    class Meta:
        verbose_name = 'Post'

    def __str__(self):
        return self.title
        