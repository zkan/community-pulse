from django.db import models

from django_extensions.db.models import TimeStampedModel


class Event(TimeStampedModel):
    name = models.CharField(max_length=300)
    description = models.TextField()
    facebook_event_id = models.CharField(max_length=30)
