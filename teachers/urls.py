
from django.urls import path
from . import views

app_name = "teachers"

urlpatterns = [
    path("", views.teacher_list, name="list"),
    path("new/", views.teacher_create, name="create"),
    path("edit/<int:pk>/", views.teacher_update, name="update"),
    path("delete/<int:pk>/", views.teacher_delete, name="delete"),
    path("<int:pk>/", views.teacher_detail, name="detail"),
]