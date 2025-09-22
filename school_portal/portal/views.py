from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course, Enrollment
from .forms import StudentForm, CourseForm, EnrollmentForm
def home(request): return render(request, "home.html")
def students_list(request):
    return render(request, "students/list.html", {"students": Student.objects.all()})
