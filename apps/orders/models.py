from django.db import models
from apps.users.models import User
from apps.events.models import Event

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    number_of_tickets = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
