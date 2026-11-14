from django.db import models
from django.utils import timezone


class Student(models.Model):
    first_name = models.CharField("Prénom", max_length=100)
    last_name = models.CharField("Nom", max_length=100)
    email = models.EmailField("Email", unique=True, null=True, blank=True)
    classe = models.CharField("Classe", max_length=10, default="L1")
    active = models.BooleanField("Statut", default=True)
    birth_date = models.DateField("Date de naissance", null=True, blank=True)
    phone = models.CharField("Téléphone", max_length=20, blank=True)
    created_at = models.DateTimeField("Inscrit le", default=timezone.now)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
