from django.contrib import admin

from .models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'event', 'created', 'modified',)
    list_filter = ('event__name', 'type',)
    search_fields = ('title',)
