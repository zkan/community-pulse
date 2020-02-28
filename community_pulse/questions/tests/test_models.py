from django.test import TestCase

from ..models import Question
from events.models import Event


class QuestionTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        event_name = 'Data Council BKK Meetup #5'
        event_description = 'There will be 3 talks regarding data engineering.'
        event_facebook_event_id = '1496228460533709'

        event = Event.objects.create(
            name=event_name,
            description=event_description,
            facebook_event_id=event_facebook_event_id,
        )

        cls.expected_title = 'How satisfied were you for the overall in this event?'
        cls.expected_event = event
        cls.expected_type = 'registration'

        cls.question = Question.objects.create(
            title=cls.expected_title,
            event=cls.expected_event,
            type=cls.expected_type,
        )

    def test_question_model_should_have_defined_fields(self):
        assert self.question.title == self.expected_title
        assert self.question.event.id == self.expected_event.id
        assert self.question.type == self.expected_type
        assert self.question.created
        assert self.question.modified

    def test_question_model_should_have_string_representation_from_title(self):
        assert self.question.__str__() == self.expected_title
