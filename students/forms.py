from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = [
            "first_name",
            "last_name",
            "email",
            "classe",
            "active",
            "birth_date",
            "phone",
        ]

        widgets = {
            "birth_date": forms.DateInput(
                attrs={"type": "date"},
                format="%Y-%m-%d"
            ),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get("phone", "")
        phone = phone.replace(" ", "")

        if phone and (not phone.isdigit() or len(phone) != 9):
            raise forms.ValidationError(
                "Le numéro de téléphone doit contenir exactement 9 chiffres."
            )

        return phone