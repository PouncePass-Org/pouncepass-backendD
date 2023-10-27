from django.http import JsonResponse
from .models import Venue

def addVenue(request):
    # logic to add venue
    return JsonResponse({"status": "Venue Added"})

def updateVenue(request, venue_id):
    # logic to update venue
    return JsonResponse({"status": "Venue Updated"})

def deleteVenue(request, venue_id):
    # logic to delete venue
    return JsonResponse({"status": "Venue Deleted"})
