from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='students'
    )

    year = models.PositiveIntegerField()
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    joined_date = models.DateField(auto_now_add=True)

    def attendance_percentage(self):
        records = self.attendance_records.all()

        total = records.count()

        if total == 0:
            return 0

        present = records.filter(status='present').count()

        return round((present / total) * 100, 2)

    def __str__(self):
        return f"{self.student_id} - {self.name}"