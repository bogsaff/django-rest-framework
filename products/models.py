from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    price = models.FloatField(default=0)