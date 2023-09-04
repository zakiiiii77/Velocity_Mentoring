from django.db import models

class Location(models.Model):
   name = models.CharField(max_length=100)
   likes = models.IntegerField(default=0)
   dislikes = models.IntegerField(default=0)

class Comment(models.Model):
   location = models.ForeignKey(Location, on_delete=models.CASCADE)
   text = models.TextField()