from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),

    path('add/', views.add_student, name='add_student'),

    path('edit/<int:student_id>/', views.edit_student, name='edit_student'),

    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),

    path('view/<int:student_id>/', views.student_detail, name='student_detail'),

    path('departments/', views.department_list, name='department_list'),

    path('departments/add/', views.add_department, name='add_department'),

    path('departments/edit/<int:department_id>/', views.edit_department, name='edit_department'),

    path('departments/delete/<int:department_id>/', views.delete_department, name='delete_department'),
]