from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path("", views.student_list, name="list"),
    path("<int:id>/", views.student_detail, name="detail"),
    path("classe/<str:classe>/", views.students_by_class, name="by_class"),
    path("<int:id>/modifier/", views.student_update, name="update"),
]