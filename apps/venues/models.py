from django.db import models

class Venue(models.Model):
    venueId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    capacity = models.IntegerField()
