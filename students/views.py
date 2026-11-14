from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Student
from .forms import StudentForm


def student_list(request):
    query = request.GET.get("q", "")
    classe = request.GET.get("classe", "")

    students = Student.objects.all()

    if query:
        students = students.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )

    if classe:
        students = students.filter(classe=classe)

    classes = Student.objects.values_list(
        "classe", flat=True
    ).distinct()

    context = {
        "students": students,
        "query": query,
        "classe": classe,
        "classes": classes,
    }

    return render(request, "students/student_list.html", context)


def student_detail(request, id):
    student = get_object_or_404(Student, id=id)

    context = {
        "student": student,
    }

    return render(request, "students/student_detail.html", context)


def students_by_class(request, classe):
    students = Student.objects.filter(classe=classe)

    context = {
        "students": students,
        "classe": classe,
        "query": "",
        "classes": Student.objects.values_list(
            "classe", flat=True
        ).distinct(),
    }

    return render(request, "students/student_list.html", context)


def student_update(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect("students:detail", id=student.id)

    else:
        form = StudentForm(instance=student)

    context = {
        "form": form,
        "student": student,
    }

    return render(request, "students/student_update.html", context)