from django.contrib import admin
from django.urls import path
from students.views import home, student_list, student_detail, about, students_by_class, teacher_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('students/', student_list, name='student_list'),
    path('students/<int:id>/', student_detail, name='student_detail'),
    path('about/', about, name='about'),
    path('students/classe/<str:classe>/', students_by_class, name='students_by_class'),
    path('teachers/', teacher_list, name='teacher_list'),
]