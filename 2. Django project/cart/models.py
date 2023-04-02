from django.db import models
from django.conf import settings


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete)
