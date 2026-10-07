from django.db import models


class Mark(models.Model):
    student = models.ForeignKey(
        'students.Student',
        on_delete=models.CASCADE,
        related_name='marks'
    )

    subject = models.ForeignKey(
        'subjects.Subject',
        on_delete=models.CASCADE,
        related_name='marks'
    )

    internal_mark = models.PositiveIntegerField(default=0)
    exam_mark = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'subject')

    @property
    def total_mark(self):
        return self.internal_mark + self.exam_mark

    @property
    def grade(self):
        total = self.total_mark

        if total >= 90:
            return 'A+'
        elif total >= 80:
            return 'A'
        elif total >= 70:
            return 'B'
        elif total >= 60:
            return 'C'
        elif total >= 50:
            return 'D'
        else:
            return 'F'

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}"
