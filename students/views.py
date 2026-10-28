from django.shortcuts import render
from django.http import Http404

# Données temporaires des étudiants
STUDENTS = [
    {"id": 1, "first_name": "Awa", "last_name": "Diop", "classe": "L1", "active": True, "phone": "77 123 45 67"},
    {"id": 2, "first_name": "Moussa", "last_name": "Fall", "classe": "L2", "active": True, "phone": "77 124 45 67"},
    {"id": 3, "first_name": "Fatou", "last_name": "Ndiaye", "classe": "L1", "active": False, "phone": "77 125 45 67"},
    {"id": 4, "first_name": "Ibrahima", "last_name": "Sow", "classe": "L3", "active": True, "phone": "77 126 45 67"},
]

# Données temporaires des enseignants
TEACHERS = [
    {"first_name": "Mamadou", "last_name": "Ba", "subject": "Mathématiques"},
    {"first_name": "Aïssatou", "last_name": "Sy", "subject": "Informatique"},
    {"first_name": "Cheikh", "last_name": "Diallo", "subject": "Anglais"},
]

def home(request):
    context = {
        "school_name": "Lycée d'Excellence de Dakar",
        "nb_classes": 12,
    }
    return render(request, "students/home.html", context)

def student_list(request):
    context = {"students": STUDENTS}
    return render(request, "students/student_list.html", context)

def student_detail(request, id):
    for student in STUDENTS:
        if student["id"] == id:
            context = {"student": student}
            return render(request, "students/student_detail.html", context)
    raise Http404("Étudiant introuvable")

def about(request):
    return render(request, "students/about.html")

def students_by_class(request, classe):
    selection = [student for student in STUDENTS if student["classe"] == classe]
    context = {"students": selection}
    return render(request, "students/student_list.html", context)

def teacher_list(request):
    context = {"teachers": TEACHERS}
    return render(request, "students/teachers.html", context)