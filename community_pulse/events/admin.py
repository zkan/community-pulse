from django.contrib import admin

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'facebook_event_id',
        'created',
        'modified',
    )
    search_fields = (
        'name',
        'facebook_event_id',
        'created',
        'modified',
    )
