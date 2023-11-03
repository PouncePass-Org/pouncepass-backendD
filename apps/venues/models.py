from django.db import models
from django.core.exceptions import ValidationError

class Venue(models.Model):
    venue_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255, default='Not Provided')
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    capacity = models.IntegerField()

    def __str__(self):
        """String representation of the Venue model."""
        return f"{self.name} ({self.city}, {self.state})"

    def clean(self):
        """Custom validation for the Venue model."""
        if self.capacity < 0:
            raise ValidationError("Capacity cannot be negative.")
