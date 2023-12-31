from django.db import models
from apps.events.models import Event
from apps.users.models import User

class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
