from django.db import models
from apps.events.models import Event
from apps.users.models import User

class Ticket(models.Model):
    ticketId = models.AutoField(primary_key=True)
    eventId = models.ForeignKey(Event, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
