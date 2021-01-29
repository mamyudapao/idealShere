from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    skill = models.CharField(max_length=200, null=True)
    


