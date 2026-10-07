from django.shortcuts import render, redirect
from .models import Subject
from students.models import Department
from teachers.models import Teacher


def subject_list(request):

    query = request.GET.get('q')

    if query:
        subjects = Subject.objects.filter(
            name__icontains=query
        ) | Subject.objects.filter(
            subject_code__icontains=query
        )
    else:
        subjects = Subject.objects.all()

    return render(
        request,
        'subjects/subject_list.html',
        {'subjects': subjects}
    )


def add_subject(request):
    departments = Department.objects.all()
    teachers = Teacher.objects.all()

    if request.method == 'POST':
        subject_code = request.POST.get('subject_code')
        name = request.POST.get('name')
        department_id = request.POST.get('department')
        teacher_id = request.POST.get('teacher')
        credits = request.POST.get('credits')
        semester = request.POST.get('semester')

        department = Department.objects.get(id=department_id)

        teacher = None
        if teacher_id:
            teacher = Teacher.objects.get(id=teacher_id)

        Subject.objects.create(
            subject_code=subject_code,
            name=name,
            department=department,
            teacher=teacher,
            credits=credits,
            semester=semester
        )

        return redirect('/subjects/')

    return render(
        request,
        'subjects/add_subject.html',
        {
            'departments': departments,
            'teachers': teachers
        }
    )

def edit_subject(request, subject_id):
    subject = Subject.objects.get(id=subject_id)

    departments = Department.objects.all()
    teachers = Teacher.objects.all()

    if request.method == 'POST':
        subject.subject_code = request.POST.get('subject_code')
        subject.name = request.POST.get('name')

        department_id = request.POST.get('department')
        subject.department = Department.objects.get(id=department_id)

        teacher_id = request.POST.get('teacher')

        if teacher_id:
            subject.teacher = Teacher.objects.get(id=teacher_id)
        else:
            subject.teacher = None

        subject.credits = request.POST.get('credits')
        subject.semester = request.POST.get('semester')

        subject.save()

        return redirect('/subjects/')

    return render(
        request,
        'subjects/edit_subject.html',
        {
            'subject': subject,
            'departments': departments,
            'teachers': teachers
        }
    )

def delete_subject(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    subject.delete()

    return redirect('/subjects/')