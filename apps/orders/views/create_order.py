from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db import transaction
from apps.orders.models import Order
from apps.events.models import Event
from apps.orders.serializers import OrderSerializer
from apps.tickets.models import Ticket
from apps.tickets.serializers import TicketSerializer
from apps.payments.models import Payment
from apps.payments.serializers import PaymentSerializer
from rest_framework import status
import logging

logger = logging.getLogger(__name__)

class CreateOrder(APIView):
    permission_classes = [AllowAny]

    @transaction.atomic
    def post(self, request):
        # Extract event details
        event_id = request.data.get('event_id')
        num_tickets = request.data.get('num_tickets')

        # Retrieve event and calculate total price
        event = Event.objects.get(pk=event_id)

        # Check if enough tickets are available
        if event.available_tickets < num_tickets:
            return Response({
                'error': 'Not enough tickets available.'
            }, status=status.HTTP_400_BAD_REQUEST)

        total_price = event.ticket_price * num_tickets

        # Create Order instance
        order = Order.objects.create(
            user=request.user,
            event=event,
            number_of_tickets=num_tickets,
            total_amount=total_price
        )

        # Create Ticket instances
        tickets = [Ticket(event=event, user=request.user, status='booked') for _ in range(num_tickets)]
        Ticket.objects.bulk_create(tickets)

        # Update the available tickets in the event
        event.available_tickets -= num_tickets
        event.save()

        # Create Payment instance
        # Here you would typically integrate with a payment gateway.
        # For simplicity, we'll just record a dummy payment.
        payment = Payment.objects.create(
            order=order,
            payment_method='credit_card',
            status='completed'
        )

        # Serialize the response
        order_serializer = OrderSerializer(order)
        tickets_serializer = TicketSerializer(tickets, many=True)
        payment_serializer = PaymentSerializer(payment)

        #print/log success here
        logger.info("Ticket successfully created.")

    # Return the response
        return Response({
            'order': order_serializer.data,
            'tickets': tickets_serializer.data,
            'payment': payment_serializer.data
        },status=status.HTTP_201_CREATED)
