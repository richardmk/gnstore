from django.db import models
from apps.core.models import BaseModel
# Create your models here.
class Contact(BaseModel):
    name = models.CharField('Name', max_length=150)
    email = models.CharField('Email', max_length=150)
    message = models.TextField('Message')

    class Meta:
        verbose_name = 'Contact'

    def __str__(self):
        return self.name
      