from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.orders.models import Order
from apps.tickets.models import Ticket
from rest_framework import status

class CancelOrderView(APIView):
    permission_classes = [AllowAny]

    def delete(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id, user=request.user)

        # Assuming that the Order model has a status field and a method to handle cancellation
        if order.status != 'cancelled':
            order.status = 'cancelled'
            order.save()

            # Here, you would typically have logic to handle ticket release.
            # For instance, update the status of the associated tickets.
            Ticket.objects.filter(order=order).update(status='cancelled')

            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'detail': 'Order already cancelled.'}, status=status.HTTP_400_BAD_REQUEST)
