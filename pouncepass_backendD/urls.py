from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include('apps.events.urls')),
    path('users/', include('apps.users.urls')),
    path('venues/', include('apps.venues.urls')),
    path('tickets/', include('apps.tickets.urls')),
    path('payments/', include('apps.payments.urls')),
    path('orders/', include('apps.orders.urls')),
]
