
from django import forms
from .models import Teacher


class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = [
            "first_name",
            "last_name",
            "email",
            "subject",
            "phone",
        ]

        labels = {
            "first_name": "Prénom",
            "last_name": "Nom",
            "email": "Adresse e-mail",
            "subject": "Matière enseignée",
            "phone": "Numéro de téléphone",
        }