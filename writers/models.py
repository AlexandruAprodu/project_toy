from django.db import models
from django.contrib.auth.models import User


class Writer(models.Model):

    name = models.OneToOneField(User, related_name='writer', on_delete=models.CASCADE)
    is_editor = models.BooleanField(default=False)


