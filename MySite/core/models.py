from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class BaseModel(models.Model):
    class Meta:
        abstract = True


class User(AbstractUser):
    pass
