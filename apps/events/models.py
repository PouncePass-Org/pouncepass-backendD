# File: events/models.py
from django.db import models
from apps.venues.models import Venue

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_tickets = models.PositiveIntegerField(default=0)
    available_tickets = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def book_ticket(self):
        if self.available_tickets > 0:
            self.available_tickets -= 1
            self.save()
            return True
        return False

    def cancel_ticket(self):
        self.available_tickets += 1
        self.save()
