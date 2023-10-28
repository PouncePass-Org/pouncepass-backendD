# File: events/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated  # Adjust the permission as needed
from rest_framework.response import Response
from ..models import Event
from ..serializers import EventSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Adjust the permission as needed
def get_all_events(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)
