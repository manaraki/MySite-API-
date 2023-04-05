from django.core.validators import MinLengthValidator
from django.db import models

from core.models import User


class Student(User):
    national_ID = models.CharField(max_length=10, validators=[MinLengthValidator(10)], null=True, blank=True)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
