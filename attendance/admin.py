from django.contrib import admin
from .models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'subject',
        'date',
        'status',
        'marked_at',
    )

    list_filter = (
        'status',
        'date',
        'subject',
    )

    search_fields = (
        'student__name',
        'student__student_id',
        'subject__name',
    )

    ordering = ('-date',)
