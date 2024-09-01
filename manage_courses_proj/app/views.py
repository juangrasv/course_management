from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def home(request):
    courses = Course.objects.all()
    return render(request, 'courseManagement.html', {"courses": courses})

def registerCourse(request):
    courseCode = request.POST['txtCode']
    courseName = request.POST['txtName']
    courseCredits = request.POST['numCredits']

    course = Course.objects.create(course_code=courseCode, name=courseName, credits=courseCredits)

    return redirect('/')

def deleteCourse(request, courseCode):
    course = Course.objects.get(course_code=courseCode)
    course.delete()

    return redirect('/')
