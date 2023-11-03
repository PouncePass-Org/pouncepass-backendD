from django.db import models
from django.db.transaction import atomic
from django.core.exceptions import ValidationError
from apps.venues.models import Venue

CATEGORY_CHOICES = [
    ('concerts', 'Concerts'),
    ('art', 'Art'),
    ('sports', 'Sports'),
    ('more', 'More'),
]

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='events')
    date_time = models.DateTimeField()
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_tickets = models.PositiveIntegerField(default=0)
    available_tickets = models.PositiveIntegerField(default=0)

    def __str__(self):
        """String representation of the Event model."""
        return self.name

    @atomic
    def book_ticket(self):
        """Book a ticket for this event."""
        if self.available_tickets <= 0:
            raise ValidationError("No tickets available to book.")
        self.available_tickets -= 1
        self.save()

    @atomic
    def cancel_ticket(self):
        """Cancel a ticket booking for this event."""
        if self.available_tickets >= self.total_tickets:
            raise ValidationError("All tickets are already available.")
        self.available_tickets += 1
        self.save()
