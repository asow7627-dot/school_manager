from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    classe = models.CharField(max_length=20)
    active = models.BooleanField(default=True)
    phone = models.CharField(max_length=20, blank=True)

    def _str_(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def _str_(self):
        return f"{self.first_name} {self.last_name}"