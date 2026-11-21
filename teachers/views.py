from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Teacher
from .forms import TeacherForm


def teacher_list(request):
    teachers = Teacher.objects.all().order_by("last_name", "first_name")

    return render(request, "students/teachers.html", {
        "teachers": teachers,
    })


def teacher_create(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "L'enseignant a été ajouté avec succès.")
            return redirect("teachers:list")
    else:
        form = TeacherForm()

    return render(request, "teachers/teacher_form.html", {"form": form})


def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)

    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request, "Modification effectuée avec succès.")
            return redirect("teachers:list")
    else:
        form = TeacherForm(instance=teacher)

    return render(request, "teachers/teacher_form.html", {"form": form})


def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)

    if request.method == "POST":
        teacher.delete()
        messages.success(request, "Enseignant supprimé avec succès.")
        return redirect("teachers:list")

    return render(request, "teachers/teacher_confirm_delete.html", {
        "teacher": teacher,
    })


def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)

    return render(request, "teachers/teacher_detail.html", {
        "teacher": teacher,
    })