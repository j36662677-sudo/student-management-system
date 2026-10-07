from django.shortcuts import render, redirect
from .models import Mark
from students.models import Student
from subjects.models import Subject


def mark_list(request):

    query = request.GET.get('q')

    if query:
        marks = Mark.objects.filter(
            student__name__icontains=query
        ) | Mark.objects.filter(
            subject__name__icontains=query
        )
    else:
        marks = Mark.objects.all()

    return render(
        request,
        'marks/mark_list.html',
        {'marks': marks}
    )


def add_mark(request):
    students = Student.objects.all()
    subjects = Subject.objects.all()

    if request.method == 'POST':
        student_id = request.POST.get('student')
        subject_id = request.POST.get('subject')
        internal_mark = request.POST.get('internal_mark')
        exam_mark = request.POST.get('exam_mark')

        student = Student.objects.get(id=student_id)
        subject = Subject.objects.get(id=subject_id)

        Mark.objects.create(
            student=student,
            subject=subject,
            internal_mark=internal_mark,
            exam_mark=exam_mark
        )

        return redirect('/marks/')

    return render(
        request,
        'marks/add_mark.html',
        {
            'students': students,
            'subjects': subjects
        }
    )

def edit_mark(request, mark_id):
    mark = Mark.objects.get(id=mark_id)

    students = Student.objects.all()
    subjects = Subject.objects.all()

    if request.method == 'POST':
        mark.student = Student.objects.get(
            id=request.POST.get('student')
        )

        mark.subject = Subject.objects.get(
            id=request.POST.get('subject')
        )

        mark.internal_mark = request.POST.get('internal_mark')
        mark.exam_mark = request.POST.get('exam_mark')

        mark.save()

        return redirect('/marks/')

    return render(
        request,
        'marks/edit_mark.html',
        {
            'mark': mark,
            'students': students,
            'subjects': subjects
        }
    )


def delete_mark(request, mark_id):
    mark = Mark.objects.get(id=mark_id)
    mark.delete()

    return redirect('/marks/')