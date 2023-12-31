from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Event
from ..serializers import EventSerializer

class GetAllEvents(APIView):

    def get(self, request, format=None):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

# And then update your urls.py to use the class-based view
