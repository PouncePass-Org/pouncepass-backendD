from django.db import models
from apps.users.models import User
from apps.events.models import Event

class Order(models.Model):
    orderId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    eventId = models.ForeignKey(Event, on_delete=models.CASCADE)
    numberOfTickets = models.IntegerField()
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2)
