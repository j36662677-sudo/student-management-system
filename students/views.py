from django.shortcuts import render, redirect
from .models import Student, Department


def student_list(request):
    query = request.GET.get('q')

    if query:
        students = Student.objects.filter(
            name__icontains=query
        ) | Student.objects.filter(
            student_id__icontains=query
        )
    else:
        students = Student.objects.all()

    return render(request, 'students/student_list.html', {
        'students': students
    })

def add_student(request):
    departments = Department.objects.all()

    if request.method == 'POST':

        student_id = request.POST.get('student_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        department_id = request.POST.get('department')
        year = request.POST.get('year')

        department = Department.objects.get(id=department_id)

        Student.objects.create(
            student_id=student_id,
            name=name,
            email=email,
            phone=phone,
            department=department,
            year=year
        )

        return redirect('/students/')

    return render(request, 'students/add_student.html', {
        'departments': departments
    })

def edit_student(request, student_id):
    student = Student.objects.get(id=student_id)
    departments = Department.objects.all()

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.phone = request.POST.get('phone')

        department_id = request.POST.get('department')
        student.department = Department.objects.get(id=department_id)

        student.year = request.POST.get('year')
        student.save()

        return redirect('/students/')

    return render(request, 'students/edit_student.html', {
        'student': student,
        'departments': departments
    })

def delete_student(request, student_id):
    student = Student.objects.get(student_id=student_id)
    student.delete()
    return redirect('/students/')

def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/student_detail.html', {
        'student': student
    })

def department_list(request):

    query = request.GET.get('q')

    if query:
        departments = Department.objects.filter(
            name__icontains=query
        ) | Department.objects.filter(
            code__icontains=query
        )
    else:
        departments = Department.objects.all()

    return render(
        request,
        'students/department_list.html',
        {'departments': departments}
    )

def add_department(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        code = request.POST.get('code')

        Department.objects.create(
            name=name,
            code=code
        )

        return redirect('/students/departments/')

    return render(
        request,
        'students/add_department.html'
    )

def edit_department(request, department_id):
    department = Department.objects.get(id=department_id)

    if request.method == 'POST':
        department.name = request.POST.get('name')
        department.code = request.POST.get('code')

        department.save()

        return redirect('/students/departments/')

    return render(
        request,
        'students/edit_department.html',
        {'department': department}
    )


def delete_department(request, department_id):
    department = Department.objects.get(id=department_id)

    department.delete()

    return redirect('/students/departments/')