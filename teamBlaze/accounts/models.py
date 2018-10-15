from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MyUser(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key= True)
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    def __str__(self):
        return self.user.username

class Car(models.Model):
    pass