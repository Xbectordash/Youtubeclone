from django.db import models

# Create your models here.


class YourModel(models.Model):
    #name = models.CharField(max_length=100)
    todo = models.TextField()
    # Add more fields as needed

