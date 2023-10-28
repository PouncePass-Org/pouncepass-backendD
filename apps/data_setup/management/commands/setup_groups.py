from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from apps.venues.models import Venue
from apps.events.models import Event

class Command(BaseCommand):
    help = 'Setup user groups and permissions'

    def handle(self, *args, **kwargs):
        # Create groups
        admin_group, created = Group.objects.get_or_create(name='Admin')
        regular_group, created = Group.objects.get_or_create(name='Regular')

        # Get permissions for Venue and Event
        venue_content_type = ContentType.objects.get_for_model(Venue)
        event_content_type = ContentType.objects.get_for_model(Event)
        venue_permissions = Permission.objects.filter(content_type=venue_content_type)
        event_permissions = Permission.objects.filter(content_type=event_content_type)

        # Combine permissions
        all_permissions = venue_permissions | event_permissions

        # Assign permissions to admin group
        admin_group.permissions.set(all_permissions)

        self.stdout.write(self.style.SUCCESS('Successfully set up groups and permissions'))
