from django.urls import path
from .views.create_order import CreateOrder
from .views.get_orders import GetOrders
from .views.get_one_order import GetOneOrder
from .views.update_order import UpdateOrder
from .views.order_confirmation import OrderConfirmation

# Dummy view is already defined correctly

urlpatterns = [
    path('order/confirmation/<int:order_id>/', OrderConfirmation.as_view(), name='order_confirmation'),
    path('create_order/', CreateOrder.as_view(), name='create_order'),
    path('get_orders/', GetOrders.as_view(), name='get_orders'),
    path('get_order/<int:order_id>/', GetOneOrder.as_view(), name='get_order'),
    path('update_order/<int:order_id>/', UpdateOrder.as_view(), name='update_order'),
]
