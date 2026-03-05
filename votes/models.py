from django.db import models
from users.models import User
from applications.models import APP


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    app = models.ForeignKey(APP, on_delete= models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add= True)
    updateAt = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.id
