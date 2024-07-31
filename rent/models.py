from django.db import models

# Create your models here.


class rentals(models.Model):
    title = models.CharField(max_length=255)
