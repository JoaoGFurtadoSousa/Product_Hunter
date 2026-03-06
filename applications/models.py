from django.db import models
from hashtags.models import Hashtags
from category.models import Category


class APP(models.Model):
    name = models.CharField(max_length= 60)
    description = models.CharField(max_length= 300)
    likes = models.IntegerField(default= 0)
    logo_app = models.ImageField(upload_to='media')
    hashtags = models.ManyToManyField(Hashtags)
    category = models.ForeignKey(Category, on_delete= models.SET_DEFAULT, default= 1)
    

    class Meta:
        indexes = [
            models.Index(fields= ['name', 'description']),
        ]

    def __str__(self):
        return self.name
