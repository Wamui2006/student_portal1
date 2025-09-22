from django import forms
from .models import Student, Course, Enrollment
class StudentForm(forms.ModelForm):
    class Meta: model = Student; fields = ["first_name", "last_name", "email"]
class CourseForm(forms.ModelForm):
    class Meta: model = Course; fields = ["code", "title", "description"]
class EnrollmentForm(forms.ModelForm):
    class Meta: model = Enrollment; fields = ["student", "course", "semester"]
