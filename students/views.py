from django.http import HttpResponse
# 1. Page d'accueil avec les liens
def home(request):
    return HttpResponse("""
        <h1>Bienvenue dans School Manager</h1>
        <ul>
            <li><a href="/students/">Voir la liste des étudiants</a></li>
            <li><a href="/students/15/">Voir l'étudiant numéro 15</a></li>
            <li><a href="/about/">Présentation de l'école</a></li>
            <li><a href="/courses/">Liste des cours</a></li>
        </ul>
    """)
# 2. Page de la liste des étudiants
def student_list(request):
    return HttpResponse("<h2>Liste des étudiants</h2><p>1. Alice<br>2. Bob<br>15. Chloé</p>")
# 3. Page détaillée d'un étudiant (URL dynamique)
def student_detail(request, id):
    return HttpResponse(f"<h2>Détail de l'étudiant numéro {id}</h2>")
# 4. Pages du défi final (Présentation et Cours)
def about(request):
    return HttpResponse("<h2>Présentation de l'école</h2><p>Bienvenue dans notre établissement scolaire.</p>")
def course_list(request):
    return HttpResponse("<h2>Liste des cours</h2><p>Mathématiques, Informatique, Anglais</p>")