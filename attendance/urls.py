from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendance_list, name='attendance_list'),
    path('add/', views.add_attendance, name='add_attendance'),
    path('edit/<int:attendance_id>/', views.edit_attendance, name='edit_attendance'),
    path('delete/<int:attendance_id>/', views.delete_attendance, name='delete_attendance'),
]