from django.http import JsonResponse
from .models import Order

def createOrder(request):
    # logic to create order
    return JsonResponse({"status": "Order Created"})

def updateOrder(request, order_id):
    # logic to update order
    return JsonResponse({"status": "Order Updated"})

def cancelOrder(request, order_id):
    # logic to cancel order
    return JsonResponse({"status": "Order Cancelled"})
