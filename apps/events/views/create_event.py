# File: events/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from ..serializers import EventSerializer

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_event(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=201)
    return Response({"status": "error", "errors": serializer.errors}, status=400)
