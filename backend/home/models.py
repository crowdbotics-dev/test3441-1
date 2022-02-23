from django.conf import settings
from django.db import models


class Testing(models.Model):
    "Generated Model"
    some = models.BigIntegerField()
    things = models.CharField(
        max_length=256,
    )
