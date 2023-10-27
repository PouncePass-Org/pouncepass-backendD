from django.http import JsonResponse
from .models import Ticket

def bookTicket(request):
    # logic to book ticket
    return JsonResponse({"status": "Ticket Booked"})

def cancelTicket(request, ticket_id):
    # logic to cancel ticket
    return JsonResponse({"status": "Ticket Cancelled"})
