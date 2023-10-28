from django.db import models

class Venue(models.Model):
    venue_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    location = models.TextField()
    capacity = models.IntegerField()
