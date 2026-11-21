
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from .models import Student
from .forms import StudentForm


# LISTE DES ÉTUDIANTS
def student_list(request):
    query = request.GET.get("q", "")
    classe = request.GET.get("classe", "")

    # Classement alphabétique par nom et prénom
    students = Student.objects.all().order_by(
        "last_name", "first_name"
    )

    # Recherche par prénom ou nom
    if query:
        students = students.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )

    # Filtrage par classe
    if classe:
        students = students.filter(classe=classe)

    # Liste des classes disponibles
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


# DÉTAILS D'UN ÉTUDIANT
def student_detail(request, id):
    student = get_object_or_404(Student, id=id)

    context = {
        "student": student,
    }

    return render(request, "students/student_detail.html", context)


# ÉTUDIANTS PAR CLASSE
def students_by_class(request, classe):
    students = Student.objects.filter(
        classe=classe
    ).order_by("last_name", "first_name")

    context = {
        "students": students,
        "classe": classe,
        "query": "",
        "classes": Student.objects.values_list(
            "classe", flat=True
        ).distinct(),
    }

    return render(request, "students/student_list.html", context)


# MODIFIER UN ÉTUDIANT
def student_update(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                f"{student} a été modifié(e) avec succès."
            )
            return redirect("students:detail", id=student.id)

    else:
        form = StudentForm(instance=student)

    context = {
        "form": form,
        "student": student,
    }

    return render(
        request,
        "students/student_update.html",
        context
    )


# AJOUTER UN ÉTUDIANT
def student_create(request):

    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            student = form.save()

            messages.success(
                request,
                f"{student} a été inscrit(e) avec succès."
            )

            return redirect("students:list")

    else:
        form = StudentForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "students/form.html",
        context
    )
    # SUPPRIMER UN ÉTUDIANT
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.delete()

        messages.success(
            request,
            "L'étudiant a été supprimé avec succès."
        )

        return redirect("students:list")

    context = {
        "student": student,
    }

    return render(
        request,
        "students/student_confirm_delete.html",
        context
    )