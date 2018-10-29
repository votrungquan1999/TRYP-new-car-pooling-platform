from django.db import models
from driver_interface.models import Post
from accounts.models import MyUser

# Create your models here.
class NeedRidePost(Post):
    my_user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=None)