from django.db import models

# Create your models here.
# tunr/models.py
class Car(models.Model):
    name = models.CharField(max_length=100, null=True)
    make = models.CharField(max_length=100, null=True)
    model = models.CharField(max_length=100, null=True)
    year = models.CharField(max_length=4, null=True)
    color = models.CharField(max_length=100, null=True)
    trim = models.CharField(max_length=100, null=True)
    photo_url = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=1000, null=True)

    def __str__(self):  
        return self.name
    

class Comment(models.Model):
    comment = models.CharField(max_length=500)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car')

    def __str__(self):
        return self.comment