from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db.models import Q
from ..models import Event
from ..serializers import EventSerializer


@api_view(['GET'])
@permission_classes([AllowAny])  # Adjust the permission as needed
def search_events(request):
    query = request.GET.get('q', '')
    events = Event.objects.filter(
        Q(name__icontains=query) |
        Q(venue__name__icontains=query) |
        Q(category__icontains=query)
    )
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)