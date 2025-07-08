from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=127, unique=True)
    birthdate = models.DateField(null=True, default=None)
    is_employee = models.BooleanField(default=False)
