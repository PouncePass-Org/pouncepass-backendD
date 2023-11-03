from rest_framework.generics import RetrieveAPIView
from apps.orders.models import Order
from apps.orders.serializers import OrderSerializer

class GetOneOrder(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'order_id'
