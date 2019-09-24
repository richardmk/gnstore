from django.db import models

# Create your models here.

class BaseModel(models.Model):
    id = models.AutoField(primary_key =True)
    state = models.BooleanField('State', default=True)
    created = models.DateTimeField('Created', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Updated', auto_now=True, auto_now_add=False)
    deleted = models.DateTimeField('Deleted', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
            #django no añadira este modelo a la base de datos


##########################################################################
##########################################################################




