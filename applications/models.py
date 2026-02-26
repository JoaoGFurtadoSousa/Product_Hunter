from django.db import models
from hashtags.models import Hashtags


class APP(models.Model):
    name = models.CharField(max_length= 60)
    description = models.CharField(max_length= 300)
    likes = models.IntegerField(default= 0)
    logo_app = models.ImageField(upload_to='media')
    hashtags = models.ManyToManyField(Hashtags)
    
    def __str__(self):
        return self.name
