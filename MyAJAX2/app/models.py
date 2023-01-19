from django.db import models

class Student(models.Model):
    sname=models.CharField(max_length=50)
    email=models.EmailField(max_length=25)
    Address=models.TextField(max_length=254)
    def __str__(self):
        return self.sname
    
