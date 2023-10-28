# File: venues/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import Venue
from ..serializers import VenueSerializer

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_venue(request, venue_id):
    venue = get_object_or_404(Venue, venue_id=venue_id)
    venue.delete()
    return Response({"status": "success"}, status=200)