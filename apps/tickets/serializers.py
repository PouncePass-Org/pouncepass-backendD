# serializers.py in /apps/orders/

from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'  # You can list fields you want to include in the API
