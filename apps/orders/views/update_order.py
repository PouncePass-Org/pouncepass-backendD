from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.orders.models import Order
from apps.orders.serializers import OrderSerializer
from rest_framework import status

class UpdateOrder(APIView):
    permission_classes = [AllowAny]

    def put(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id, user=request.user)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            #create some useful print statements
            print("Update Order")
            print(order)
            return Response(serializer.data)
        #create some useful print statements to confirm success
        print("serializer wasn't valid")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
