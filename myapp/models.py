from django.db import models

class Mydata(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    telephone = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    marital_status = models.CharField(max_length=20)
    email = models.EmailField()


    def __str__(self):
        return self.name 