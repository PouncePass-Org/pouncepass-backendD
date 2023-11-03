# apps/venues/views/create_venue.py

from rest_framework import generics
from ..models import Venue
from ..serializers import VenueSerializer

class CreateVenue(generics.CreateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
