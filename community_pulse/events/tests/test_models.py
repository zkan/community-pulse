from django.test import TestCase

from ..models import Event


class EventTest(TestCase):
    def test_event_model_should_have_defined_fields(self):
        expected_name = 'Data Council BKK Meetup #5'
        expected_description = 'There will be 3 talks regarding data engineering.'
        expected_facebook_event_id = '1496228460533709'

        event = Event.objects.create(
            name=expected_name,
            description=expected_description,
            facebook_event_id=expected_facebook_event_id,
        )

        assert event.name == expected_name
        assert event.description == expected_description
        assert event.facebook_event_id == expected_facebook_event_id
