from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'question_counts']
    search_fields = ['title__startswith']

    @admin.display(ordering='question_counts')
    def question_counts(self, category):
        url = reverse('admin:poll_question_changelist') + '?' + \
            urlencode({'category_id': str('category.id')})
        return format_html("<a href='{}'>{}</a>", url, category.question_counts)

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(question_counts=Count('questions'))


class ChoiceInline(admin.TabularInline):
    model = models.Choice


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_select_related = ['category', 'author']
    list_display = ['text', 'category', 'author',
                    'comment', 'date_created', 'updated']
    autocomplete_fields = ['category', 'author']
    inlines = [ChoiceInline]


class AddressInline(admin.StackedInline):
    model = models.Address


@admin.register(models.Respondant)
class RespondantAdmin(admin.ModelAdmin):
    list_select_related = ['user']
    list_display = ['user', 'birth_date', 'occupation']
    autocomplete_fields = ['user']
    inlines = [AddressInline]
