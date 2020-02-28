from django.contrib import admin
from django.test import TestCase

from ..admin import QuestionAdmin
from ..models import Question


class QuestionAdminTest(TestCase):
    def test_admin_should_be_registered(self):
        assert isinstance(admin.site._registry[Question], QuestionAdmin)

    def test_admin_should_set_list_display(self):
        expected = ('title', 'event', 'created', 'modified',)

        assert QuestionAdmin.list_display == expected

    def test_admin_should_set_list_filter(self):
        expected = ('event__name', 'type',)

        assert QuestionAdmin.list_filter == expected

    def test_admin_should_set_search_fields(self):
        expected = ('title',)

        assert QuestionAdmin.search_fields == expected
