from django.db import models


class Teacher(models.Model):
    teacher_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    department = models.ForeignKey(
        'students.Department',
        on_delete=models.CASCADE,
        related_name='teachers'
    )
    designation = models.CharField(max_length=100)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.teacher_id} - {self.name}"
