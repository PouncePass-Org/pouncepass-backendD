# File: venues/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import Venue
from ..serializers import VenueSerializer

# ... (rest of your code)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_venue(request, venue_id):
    venue = get_object_or_404(Venue, venue_id=venue_id)
    serializer = VenueSerializer(venue, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=200)
    return Response({"status": "error", "errors": serializer.errors}, status=400)
