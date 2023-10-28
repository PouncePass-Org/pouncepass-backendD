# File: /Users/dobsondunavant/Documents/GitHub/pouncepass-backendD/apps/venues/urls.py

from django.urls import path
from .views.create_venue import create_venue
from .views.delete_venue import delete_venue
from .views.get_all_venues import get_all_venues
from .views.update_venue import update_venue

urlpatterns = [
    path('create_venue/', create_venue),
    path('delete_venue/<int:venue_id>/', delete_venue),
    path('all_venues/', get_all_venues),
    path('update_venue/<int:venue_id>/', update_venue)
]
