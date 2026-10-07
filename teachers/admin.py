from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'teacher_id',
        'name',
        'email',
        'department',
        'designation',
    )

    list_filter = (
        'department',
        'designation',
    )

    search_fields = (
        'teacher_id',
        'name',
        'email',
    )