# apps/events/views/create_event.py

from rest_framework import generics
from ..models import Event
from ..serializers import EventSerializer

class CreateEvent(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
