from django.db import models
class Student(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    def __str__(self): return f"{self.first_name} {self.last_name}"
class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    def __str__(self): return f"{self.code} — {self.title}"
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=20, default="2025-1")
    class Meta: unique_together = ("student", "course")
    def __str__(self): return f"{self.student} → {self.course}"
