# File: /Users/dobsondunavant/Documents/GitHub/pouncepass-backendD/apps/events/urls.py

from django.urls import path
from .views.create_event import create_event
from .views.update_event import update_event
from .views.delete_event import delete_event
from .views.get_all_events import get_all_events
from .views.get_event import get_event

urlpatterns = [
    path('create_event/', create_event),
    path('update/<int:event_id>/', update_event),
    path('delete/<int:event_id>/', delete_event),
    path('all_events/', get_all_events, name='get_all_events'),
    path('events/<int:event_id>/', get_event, name='get_event')
]
