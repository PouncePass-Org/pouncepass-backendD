from django.http import JsonResponse
from .models import Payment

def makePayment(request):
    # logic to make payment
    return JsonResponse({"status": "Payment Made"})

def refundPayment(request, payment_id):
    # logic to refund payment
    return JsonResponse({"status": "Payment Refunded
