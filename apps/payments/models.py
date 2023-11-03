from django.db import models
from apps.orders.models import Order

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
