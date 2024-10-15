from django.db import models
from django.db.models import Model 

# Create your models here.
class Photo(models.Model):
    upload = models.ImageField(upload_to ='uploads/')