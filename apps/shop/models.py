from django.db import models
from apps.core.models import *
# Create your models here.

class Category(BaseModel):
    name = models.CharField('Category', max_length=100, unique= True)
    image = models.ImageField('Image', upload_to='product_category/')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Sex(BaseModel):
    sex = models.CharField('Sex', max_length=50)
    image = models.ImageField('Image', upload_to='sex_product', max_length=250)

    class Meta:
        verbose_name: 'Sex'

    def __str__(self):
        return self.sex
    


class Product(BaseModel):
    name = models.CharField('Name', max_length=50)
    description = models.CharField('Description', max_length=250)
    image = models.ImageField('Product', upload_to='product/')
    price = models.DecimalField('Price', max_digits=11, decimal_places=2)
    stock = models.SmallIntegerField('Stock')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE)
    promotion = models.BooleanField('Promotion',default=False)

    class Meta:
        verbose_name = 'Product'

    def __str__(self):
        return self.name
    