from django.shortcuts import render
from students.models import Student
from teachers.models import Teacher


def home(request):
    context = {
        "school_name": "Lycée d'Excellence de Dakar",
        "nb_classes": Student.objects.values("classe").distinct().count(),
        "nb_students": Student.objects.count(),
        "nb_teachers": Teacher.objects.count(),
    }

    return render(request, "students/home.html", context)


def about(request):
    return render(request, "students/about.html")
