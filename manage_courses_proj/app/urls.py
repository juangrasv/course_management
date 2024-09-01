from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('registerCourse/', views.registerCourse, name='register_course'),
    path('deleteCourse/<courseCode>/', views.deleteCourse, name='delete_course')
]
