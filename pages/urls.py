from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
     path("notebook-teranga/", views.notebook_teranga, name="notebook_teranga"),
    path("rapport-teranga/", views.rapport_teranga_pdf, name="rapport_teranga"),
    path("slide/<int:numero>/", views.afficher_slide, name="afficher_slide"),
]
