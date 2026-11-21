import os
import re
from django.conf import settings
from django.http import FileResponse, Http404
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

def rapport_teranga_pdf(request):
    return render(request, "students/rapport.html")
def afficher_slide(request, numero):
    dossier_base = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "students", "static", "students"))
    images = []
    for racine, dossiers, fichiers in os.walk(dossier_base):
        for f in fichiers:
            if f.lower().endswith((".png", ".jpg", ".jpeg")):
                images.append(os.path.join(racine, f))
    images.sort(key=lambda chemin: [int(t) if t.isdigit() else t.lower() for t in re.split(r'(\d+)', os.path.basename(chemin))])
    if 1 <= numero <= len(images):
        with open(images[numero - 1], "rb") as img_file:
            return HttpResponse(img_file.read(), content_type="image/png")
    raise Http404(f"Slide {numero} introuvable dans {dossier_base}")
def notebook_teranga(request):
    return render(request, "students/notebook.html")
