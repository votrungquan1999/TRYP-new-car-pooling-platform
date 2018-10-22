from django.db import models


# Create your models here.
class Feedback(models.Model):
    rating = models.CharField(max_length=2)
    feedback = models.TextField(blank=True, null=True)
