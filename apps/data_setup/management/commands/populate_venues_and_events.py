from django.core.management.base import BaseCommand
import random
from datetime import timedelta
from django.utils import timezone
from apps.venues.models import Venue
from apps.events.models import Event

class Command(BaseCommand):
    help = 'Populate the database with venues and events'

    def handle(self, *args, **kwargs):
        self.populate_venues()
        self.populate_events()

    def populate_venues(self, n=10):
        for i in range(n):
            Venue.objects.create(
                name=f"Venue {i}",
                location=f"Location {i}",
                capacity=random.randint(100, 1000)
            )
        self.stdout.write(self.style.SUCCESS(f'Successfully added {n} venues'))

    def populate_events(self, n=30):
        venues = list(Venue.objects.all())
        categories = ['concerts', 'art', 'sports', 'more']
        for i in range(n):
            venue = random.choice(venues)
            category = random.choice(categories)
            event_date = timezone.now() + timedelta(days=random.randint(1, 365))
            total_tickets = random.randint(50, venue.capacity)
            Event.objects.create(
                name=f"Event {i}",
                description=f"Description {i}",
                category=category,
                venue=venue,
                date_time=event_date,
                ticket_price=random.uniform(10.0, 100.0),
                total_tickets=total_tickets,
                available_tickets=total_tickets
            )
        self.stdout.write(self.style.SUCCESS(f'Successfully added {n} events'))
