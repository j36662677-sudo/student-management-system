from django.contrib import admin
from .models import Department, Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'student_id',
        'name',
        'email',
        'department',
        'year',
        'attendance_percentage',
    )

    list_filter = (
        'department',
        'year',
    )

    search_fields = (
        'student_id',
        'name',
        'email',
    )