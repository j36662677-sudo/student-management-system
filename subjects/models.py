from django.db import models


class Subject(models.Model):
    subject_code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)

    department = models.ForeignKey(
        'students.Department',
        on_delete=models.CASCADE,
        related_name='subjects'
    )

    teacher = models.ForeignKey(
        'teachers.Teacher',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subjects'
    )

    credits = models.PositiveIntegerField(default=3)

    semester = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.subject_code} - {self.name}"
