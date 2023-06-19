from django.db import models


# Create your models here.


class announcement(models.Model):
    name= models.CharField(max_length=200)
    desc= models.TextField(max_length=300)
    feedback= models.TextField(max_length=200)
    date= models.DateTimeField("date published")
    


