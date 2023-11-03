from django.db import models
from django.core.exceptions import ValidationError

class Venue(models.Model):
    venue_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255, default='Not Provided')
    capacity = models.IntegerField()

    def __str__(self):
        """String representation of the Venue model."""
        return f"{self.name} ({self.venue_id}, {self.location}, {self.capacity})"

    def clean(self):
        """Custom validation for the Venue model."""
        if self.capacity < 0:
            raise ValidationError("Capacity cannot be negative.")
