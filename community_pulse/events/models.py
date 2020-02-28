from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    facebook_event_id = models.CharField(max_length=30)
