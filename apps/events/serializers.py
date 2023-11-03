# events/serializers.py

from rest_framework import serializers
from .models import Event
from ..venues.serializers import VenueSerializer  # Adjust the import path based on your project structure

class EventSerializer(serializers.ModelSerializer):
    venue = VenueSerializer(read_only=True)

    class Meta:
        model = Event
        fields = '__all__'
        extra_kwargs = {
            'category': {
                'required': True,
                'allow_blank': False,
                'allow_null': False,
            }
        }
