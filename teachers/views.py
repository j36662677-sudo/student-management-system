from django.shortcuts import render, redirect

from .models import Teacher
from students.models import Department


def teacher_list(request):

    query = request.GET.get('q')

    if query:
        teachers = Teacher.objects.filter(
            name__icontains=query
        ) | Teacher.objects.filter(
            teacher_id__icontains=query
        ) | Teacher.objects.filter(
            email__icontains=query
        )
    else:
        teachers = Teacher.objects.all()

    return render(
        request,
        'teachers/teacher_list.html',
        {'teachers': teachers}
    )


def add_teacher(request):
    departments = Department.objects.all()

    if request.method == 'POST':
        teacher_id = request.POST.get('teacher_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        department_id = request.POST.get('department')
        designation = request.POST.get('designation')

        department = Department.objects.get(id=department_id)

        Teacher.objects.create(
            teacher_id=teacher_id,
            name=name,
            email=email,
            phone=phone,
            department=department,
            designation=designation
        )

        return redirect('/teachers/')

    return render(
        request,
        'teachers/add_teacher.html',
        {'departments': departments}
    )


def edit_teacher(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    departments = Department.objects.all()

    if request.method == 'POST':
        teacher.name = request.POST.get('name')
        teacher.email = request.POST.get('email')
        teacher.phone = request.POST.get('phone')
        teacher.department = Department.objects.get(
            id=request.POST.get('department')
        )
        teacher.designation = request.POST.get('designation')

        teacher.save()

        return redirect('/teachers/')

    return render(
        request,
        'teachers/edit_teacher.html',
        {
            'teacher': teacher,
            'departments': departments
        }
    )    

def delete_teacher(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    teacher.delete()

    return redirect('/teachers/')