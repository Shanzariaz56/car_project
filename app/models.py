from django.db import models

# Create your models here.
class Car(models.Model):
    owner_name=models.CharField(max_length=200)
    car_model=models.CharField(max_length=200)
    color=models.CharField(max_length=255)
    price=models.PositiveIntegerField()
    year=models.IntegerField()
