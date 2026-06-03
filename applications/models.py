from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from hashtags.models import Hashtags
from category.models import Category


class APP(models.Model):
    name = models.CharField(max_length= 60)
    description = models.CharField(max_length= 300)
    likes = models.IntegerField(validators= [MinValueValidator(1)])
    logo_app = models.ImageField(upload_to='media')
    hashtags = models.ManyToManyField(Hashtags)
    category = models.ForeignKey(Category, on_delete= models.SET_DEFAULT, default= 1)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields= ['name', 'description']),
        ]
    

    def __str__(self):
        return self.name
