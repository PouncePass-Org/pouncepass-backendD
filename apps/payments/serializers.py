# serializers.py in /apps/payments/

from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'  # You can list fields you want to include in the API
