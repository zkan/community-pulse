from django.db import models

from django_extensions.db.models import TimeStampedModel

from events.models import Event


class Question(TimeStampedModel):
    QUESTION_TYPES = (
        ('registration', 'Registration'),
        ('feedback', 'Feedback'),
    )

    title = models.CharField(max_length=300)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    type = models.CharField(max_length=30, choices=QUESTION_TYPES)

    def __str__(self):
        return self.title
