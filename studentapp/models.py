from django.db import models

# Create your models here

class studentdb(models.Model):
    studentname=models.CharField(max_length=100,null=True,blank=True)
    Age=models.IntegerField(null=True,blank=True)
    Phonenum=models.IntegerField(null=True,blank=True)
    Bloodgroup=models.CharField(max_length=20,null=True,blank=True)


