from django.db import models

class Registration(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    
class Login(models.Model):
    email=models.EmailField()
    contact=models.IntegerField()
