from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Cards(models.Model):
    IMG = models.ImageField(upload_to='media')
    Name = models.CharField(max_length= 15)
    Details = models.TextField()
    userid = models.IntegerField(null=True)
    catid = models.IntegerField(null=True)
    #parent = models.ForeignKey("Cards", on_delete=models.CASCADE, null= True, blank= True)
    created_at = models.DateTimeField(default = timezone.now)


class Category(models.Model):
    Name = models.CharField(max_length= 31)
    userid = models.IntegerField(null=True)
    created_at = models.DateTimeField(default = timezone.now)
    #Card = models.ForeignKey(Cards, on_delete=models.CASCADE)

class Userdet(models.Model):
    userid = models.IntegerField()
    userIMG = models.ImageField(upload_to='media')
    userphone = models.IntegerField(null=True)

