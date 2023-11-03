# serializers.py in /apps/orders/

from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'  # You can list fields you want to include in the API
