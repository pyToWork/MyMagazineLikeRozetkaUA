from django.db import models

# Create your models here.
class Subcriber(models.Model):
     email=models.EmailField()
     name=models.CharField(max_length=128)
     def __str__(self):
          return "Username: %s , Email :  %s , id:  %s " % (self.name, self.email,self.id)
