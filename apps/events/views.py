from django.http import JsonResponse
from .models import Event

def createEvent(request):
    # logic to create event
    return JsonResponse({"status": "Event Created"})

def updateEvent(request, event_id):
    # logic to update event
    return JsonResponse({"status": "Event Updated"})

def deleteEvent(request, event_id):
    # logic to delete event
    return JsonResponse({"status": "Event Deleted"})
