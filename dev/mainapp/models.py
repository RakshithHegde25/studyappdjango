from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name=models.CharField(max_length=50)


    def __str__(self):
        return self.name
    

class Rooms(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    host=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=50)
    description=models.TextField(null=True, blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name
class Message(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(Rooms,on_delete=models.CASCADE)
    body=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.body[0:50]


# Create your models here.
