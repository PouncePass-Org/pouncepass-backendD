# order_confirmation.py in /apps/orders/views/

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.orders.models import Order
from apps.tickets.models import Ticket
from apps.payments.models import Payment
from apps.orders.serializers import OrderSerializer
from apps.tickets.serializers import TicketSerializer
from apps.payments.serializers import PaymentSerializer
from django.shortcuts import get_object_or_404
import logging

logger = logging.getLogger(__name__)

class OrderConfirmation(APIView):
    permission_classes = [AllowAny]

    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id, user=request.user)
        tickets = Ticket.objects.filter(order=order)
        payments = Payment.objects.filter(order=order)

        order_serializer = OrderSerializer(order)
        tickets_serializer = TicketSerializer(tickets, many=True)
        payments_serializer = PaymentSerializer(payments, many=True)

        #create some useful print statements to confirm success
        logger.debug("Order Confirmation")
        logger.debug(f"Order: {order}")
        logger.debug(f"Tickets: {tickets}")
        logger.debug(f"Payments: {payments}")

        return Response({
            'order': order_serializer.data,
            'tickets': tickets_serializer.data,
            'payments': payments_serializer.data
        })