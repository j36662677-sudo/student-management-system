from django.urls import path
from . import views

urlpatterns = [
    path('', views.mark_list, name='mark_list'),
    path('add/', views.add_mark, name='add_mark'),
    path('edit/<int:mark_id>/', views.edit_mark, name='edit_mark'),
    path('delete/<int:mark_id>/', views.delete_mark, name='delete_mark'),
]