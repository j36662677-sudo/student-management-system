from django.urls import path
from . import views

urlpatterns = [
    path('', views.subject_list, name='subject_list'),
    path('add/', views.add_subject, name='add_subject'),
    path('edit/<int:subject_id>/', views.edit_subject, name='edit_subject'),
    path('delete/<int:subject_id>/', views.delete_subject, name='delete_subject'),
]