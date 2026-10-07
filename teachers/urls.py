from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher_list, name='teacher_list'),
    path('add/', views.add_teacher, name='add_teacher'),
    path('edit/<int:teacher_id>/', views.edit_teacher, name='edit_teacher'),
    path('delete/<int:teacher_id>/', views.delete_teacher, name='delete_teacher'),
]