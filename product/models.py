from django.db import models

# Create your models here.

class Compnay(models.Model):
    companyName = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.companyName

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    description = models.TextField()
    company = models.ForeignKey(Compnay, on_delete=models.CASCADE,related_name='products',null=True,blank=True)