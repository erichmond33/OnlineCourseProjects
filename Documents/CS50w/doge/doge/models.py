from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class ABI(models.Model):
    index = models.IntegerField(blank=False, default=-1)
    body = models.JSONField(blank=True)

    def __str__(self):
        return f"{self.index} \n {self.body}"