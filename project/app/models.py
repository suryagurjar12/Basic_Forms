from django.db import models

class StudentModel(models.Model):
    fname=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    password=models.CharField(max_length=20)
    
    
    
class QureyModel(models.Model):
    name=models.CharField(max_length=49)
    email=models.EmailField()
    qurey=models.CharField(max_length=40) 
