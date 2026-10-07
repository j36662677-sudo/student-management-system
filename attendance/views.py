from django.shortcuts import render, redirect
from .models import Attendance
from students.models import Student
from subjects.models import Subject


def attendance_list(request):

    query = request.GET.get('q')

    if query:
        attendance = Attendance.objects.filter(
            student__name__icontains=query
        ) | Attendance.objects.filter(
            subject__name__icontains=query
        )
    else:
        attendance = Attendance.objects.all()

    return render(
        request,
        'attendance/attendance_list.html',
        {'attendance': attendance}
    )


def add_attendance(request):
    students = Student.objects.all()
    subjects = Subject.objects.all()

    if request.method == 'POST':
        student_id = request.POST.get('student')
        subject_id = request.POST.get('subject')
        date = request.POST.get('date')
        status = request.POST.get('status')

        student = Student.objects.get(id=student_id)
        subject = Subject.objects.get(id=subject_id)

        Attendance.objects.create(
            student=student,
            subject=subject,
            date=date,
            status=status
        )

        return redirect('/attendance/')

    return render(
        request,
        'attendance/add_attendance.html',
        {
            'students': students,
            'subjects': subjects
        }
    )

def edit_attendance(request, attendance_id):
    attendance = Attendance.objects.get(id=attendance_id)

    students = Student.objects.all()
    subjects = Subject.objects.all()

    if request.method == 'POST':
        attendance.student = Student.objects.get(
            id=request.POST.get('student')
        )

        attendance.subject = Subject.objects.get(
            id=request.POST.get('subject')
        )

        attendance.date = request.POST.get('date')
        attendance.status = request.POST.get('status')

        attendance.save()

        return redirect('/attendance/')

    return render(
        request,
        'attendance/edit_attendance.html',
        {
            'attendance': attendance,
            'students': students,
            'subjects': subjects
        }
    )

def delete_attendance(request, attendance_id):
    attendance = Attendance.objects.get(id=attendance_id)
    attendance.delete()

    return redirect('/attendance/')