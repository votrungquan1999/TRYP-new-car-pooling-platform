from django.db import models

# Create your models here.
class Users(models.Model):
    fname = models.CharField(max_length = 40)
    lname = models.CharField(max_length = 40)
    username = models.CharField(max_length = 250)
    password = models.CharField(max_length = 40)
    email = models.CharField(max_length = 50)
    def __str__(self):
        return self.fname + self.lname
