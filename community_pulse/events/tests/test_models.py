from django.test import TestCase

from ..models import Event


class EventTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.expected_name = 'Data Council BKK Meetup #5'
        cls.expected_description = 'There will be 3 talks regarding data engineering.'
        cls.expected_facebook_event_id = '1496228460533709'

        cls.event = Event.objects.create(
            name=cls.expected_name,
            description=cls.expected_description,
            facebook_event_id=cls.expected_facebook_event_id,
        )

    def test_event_model_should_have_defined_fields(self):
        assert self.event.name == self.expected_name
        assert self.event.description == self.expected_description
        assert self.event.facebook_event_id == self.expected_facebook_event_id
        assert self.event.created
        assert self.event.modified

    def test_event_model_should_have_string_representation_from_name(self):
        assert self.event.__str__() == self.expected_name
