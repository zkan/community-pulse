from django.contrib import admin
from django.test import TestCase

from ..admin import EventAdmin
from ..models import Event


class EventAdminTest(TestCase):
    def test_admin_should_be_registered(self):
        assert isinstance(admin.site._registry[Event], EventAdmin)

    def test_admin_should_set_list_display(self):
        expected = (
            'name',
            'facebook_event_id',
        )
        assert EventAdmin.list_display == expected

    def test_admin_should_set_search_fields(self):
        expected = (
            'name',
            'facebook_event_id',
        )
        assert EventAdmin.search_fields == expected
