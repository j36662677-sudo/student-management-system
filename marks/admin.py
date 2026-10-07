from django.contrib import admin
from .models import Mark


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'subject',
        'internal_mark',
        'exam_mark',
        'total_mark',
        'grade',
    )

    list_filter = (
        'subject',
    )

    search_fields = (
        'student__name',
        'student__student_id',
        'subject__name',
    )
