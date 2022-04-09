from django.db import models

class Country2(models.Model):
    flag = models.CharField(max_length=200)
    cioc = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=100)
    callingCodes = models.CharField(max_length=50)
    capital = models.CharField(max_length=100,null=True)
    region = models.CharField(max_length=100,null=True)
    population = models.CharField(max_length = 100,null = True)
    timezone = models.CharField(max_length= 50, null=True)

    def __str__(self):
        return self.name