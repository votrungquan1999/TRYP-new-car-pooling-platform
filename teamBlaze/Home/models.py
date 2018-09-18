from django.db import models

# Create your models here.
class Users(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 250)
    pass
