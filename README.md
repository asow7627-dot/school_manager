# School Manager
Application web développée avec Django permettant de consulter et gérer les étudiants d'une école.
## Description
Projet réalisé dans le cadre de la Séance 1 : « De la requête web à notre première application Django ».
L'application met en place une architecture MVC/MVT, avec des vues HTTP et le routage d'URLs statiques et dynamiques.
## Prérequis
- Python 3.10 ou supérieur
- Git
- PowerShell ou Terminal
## Installation
1. Cloner le dépôt :
```bash
git clone <URL_DU_DEPOT>
cd school_manager
## Réponses aux questions théoriques (Section 44)
1. **Pourquoi un environnement virtuel ?**  
   Pour isoler les dépendances et versions de bibliothèques propres à ce projet, évitant les conflits avec d'autres projets.
2. **Pourquoi Django a besoin de Python ?**  
   Django est un framework entièrement écrit en Python ; l'interpréteur Python est indispensable pour exécuter son code.
3. **Différence entre un projet et une application Django ?**  
   Un projet est le conteneur global (configuration, base de données, routes principales). Une application est un module métier spécifique et réutilisable (ex: `students`).
4. **Quel est le rôle de `urls.py` ?**  
   C'est l'aiguilleur d'adresses (routeur) : il associe chaque URL demandée à la fonction vue correspondante.
5. **Quel est le rôle de `views.py` ?**  
   C'est le contrôleur : il reçoit la requête HTTP, effectue la logique et retourne une réponse HTTP au navigateur.
6. **Que se passe-t-il lorsque le navigateur demande `/students/` ?**  
   Le navigateur envoie une requête HTTP GET -> Django consulte `urls.py` -> appelle la fonction `student_list` dans `views.py` -> la fonction renvoie une `HttpResponse` affichée dans le navigateur.
7. **Pourquoi utilise-t-on Git ?**  
   Pour suivre l'historique des modifications, sécuriser le code et collaborer facilement.



   ## Questions de validation (Séance 2)

### 1. Différence entre HttpResponse et render() ?
`HttpResponse` renvoie du texte brut ou du HTML sous forme de chaîne de caractères en Python. `render()` charge un template HTML, lui injecte les données de contexte et renvoie une page web complète.

### 2. Les trois arguments de render()
- `request` : la requête HTTP reçue par la vue (obligatoire).
- `template_name` : le chemin vers le template HTML (ex. `"students/home.html"`).
- `context` : le dictionnaire de données envoyé au template (facultatif).

### 3. Pourquoi students/templates/students/ ?
Pour créer un espace de noms (namespace) et éviter les conflits si plusieurs applications ont un template portant le même nom.

### 4. Différence entre {{ ... }} et {% ... %} ?
- `{{ ... }}` sert à **afficher une valeur** (variable ou filtre).
- `{% ... %}` sert à **exécuter une logique** (boucle `for`, condition `if`, tag `url`, héritage `extends`).

### 5. Pourquoi {% url 'student_list' %} plutôt que /students/ ?
Pour éviter les liens codés en dur. Si l'URL change dans `urls.py`, tous les templates se mettent à jour automatiquement.

### 6. À quoi servent {% extends %} et {% block %} ?
- `{% extends %}` permet à un template d'hériter d'un gabarit de base (`base.html`).
- `{% block %}` définit des blocs que le template enfant peut personnaliser.

### 7. Pourquoi la vue ne doit-elle pas contenir de HTML ?
Pour respecter le principe de séparation des responsabilités : la vue traite les données et la logique (Python), tandis que le template gère l'affichage (HTML/CSS).