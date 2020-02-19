from django.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length = 200)
    hotel_img = models.ImageField(upload_to='image/')
