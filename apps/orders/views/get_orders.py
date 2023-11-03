from rest_framework.generics import ListAPIView
from apps.orders.models import Order
from apps.orders.serializers import OrderSerializer

class GetOrders(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
