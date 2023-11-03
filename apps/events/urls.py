# File: /Users/dobsondunavant/Documents/GitHub/pouncepass-backendD/apps/events/urls.py

from django.urls import path
from .views.create_event import CreateEvent
from .views.update_event import update_event
from .views.delete_event import delete_event
from .views.get_all_events import GetAllEvents
from .views.get_event import get_event

urlpatterns = [
    path('create/', CreateEvent.as_view(), name='create_order'),
    path('update/<int:event_id>/', update_event),
    path('delete/<int:event_id>/', delete_event),
    path('events/', GetAllEvents.as_view(), name='get_all_events'),
    path('event/<int:event_id>/', get_event, name='get_event')
]
