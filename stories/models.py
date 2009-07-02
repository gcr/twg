from django.db import models
from django.contrib.auth.models import User

class Story(models.Model):
    name = models.CharField(max_length = 50)
    
class Fragment(models.Model):
    text = models.CharField(max_length = 50)
    date = models.DateTimeField()
    author = models.ForeignKey(User)
    story = models.ForeignKey(Story)
