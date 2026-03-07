from django.db import models
from applications.models import APP
from django.core.validators import MinValueValidator, MaxValueValidator




class APPReview(models.Model):
    app = models.ForeignKey(APP, on_delete= models.CASCADE, related_name= "app")
    stars = models.IntegerField(validators= [
        MinValueValidator(1, message= "Quantity must be at least 1."),
        MaxValueValidator(5, message= "Quantity cannot exceed 5")
        ]
        )

    