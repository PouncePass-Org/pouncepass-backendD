# File: events/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import Event
from ..serializers import EventSerializer

# ... (rest of your code)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_event(request, event_id):
    event = get_object_or_404(Event, event_id=event_id)
    serializer = EventSerializer(event, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=200)
    return Response({"status": "error", "errors": serializer.errors}, status=400)
