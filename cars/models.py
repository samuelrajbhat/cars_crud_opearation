from django.db import models

# Create your models here.

class Cars(models.Model):
    id = models.AutoField(primary_key=True)
    car_name = models.CharField(max_length= 100)
    car_version = models.CharField(max_length=3)
    car_model = models.CharField(max_length= 15)
    car_company = models.CharField(max_length= 100)
    car_manufactured_year = models.DateField(null= True)