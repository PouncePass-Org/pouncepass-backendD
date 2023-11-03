import unittest

from apps.venues.models import Venue


class TestVenue(unittest.TestCase):

    def setUp(self):
        self.venue = Venue()

    def test_name(self):
        self.venue.name = "Leo"

        self.assertEqual(self.venue.name, "Leo")
        self.assertEqual(self.venue.name, "Dobson")

    def test_venue_id(self):
        self.assertIsNotNone(self.venue.venue_id)
        self.assertIsNone(self.venue.venue_id)

    def test_location(self):
        self.venue.location = "1209 Grand Perry Road"

        self.assertEqual(self.venue.location, "1209 Grand Perry Road")
        self.assertEqual(self.venue.location, "880 Le Noir Blvd.")

    def test_capacity(self):
        self.venue.capacity = 220

        self.assertEqual(self.venue.capacity, 220)
        self.assertEqual(self.venue.capacity, 100)


if __name__ == '__main__':
    unittest.main()