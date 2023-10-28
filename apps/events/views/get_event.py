# File: events/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny  # Adjust the permission as needed
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import Event
from ..serializers import EventSerializer

@api_view(['GET'])
@permission_classes([AllowAny])  # Adjust the permission as needed
def get_event(request, event_id):
    event = get_object_or_404(Event, event_id=event_id)
    serializer = EventSerializer(event)
    return Response(serializer.data)

# In your urls.py under events app
# path('events/<int:event_id>/', views.get_event, name='get_event'),
