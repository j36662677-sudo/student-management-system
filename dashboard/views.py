from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from students.models import Student, Department
from teachers.models import Teacher
from subjects.models import Subject
from attendance.models import Attendance
from marks.models import Mark


@login_required
def dashboard(request):

    context = {
        'total_students': Student.objects.count(),
        'total_teachers': Teacher.objects.count(),
        'total_subjects': Subject.objects.count(),
        'total_departments': Department.objects.count(),
        'total_attendance': Attendance.objects.count(),
        'total_marks': Mark.objects.count(),
    }

    return render(
        request,
        'dashboard/dashboard.html',
        context
    )