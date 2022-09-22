from django.db import models
from django.forms.fields import CharField

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    pic = models.FileField(upload_to='foods')

    def __str__(self):
        return self.name

class FoodList(models.Model):
    pic = models.FileField(upload_to='foodlist')
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name