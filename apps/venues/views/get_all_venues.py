# File: venues/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated  # Adjust the permission as needed
from rest_framework.response import Response
from ..models import Venue
from ..serializers import VenueSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Adjust the permission as needed
def get_all_venues(request):
    venues = Venue.objects.all()
    serializer = VenueSerializer(venues, many=True)
    return Response(serializer.data)
