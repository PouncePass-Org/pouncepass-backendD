from django.db import models
from apps.orders.models import Order

class Payment(models.Model):
    paymentId = models.AutoField(primary_key=True)
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE)
    paymentMethod = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
