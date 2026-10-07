from django.contrib import admin
from .models import Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        'subject_code',
        'name',
        'department',
        'teacher',
        'credits',
        'semester',
    )

    list_filter = (
        'department',
        'teacher',
        'semester',
    )

    search_fields = (
        'subject_code',
        'name',
    )
