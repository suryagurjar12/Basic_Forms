from django.db import models

class StudentModel(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    password=models.IntegerField()
    
