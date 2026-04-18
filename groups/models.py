from django.db import models
from django.conf import settings

class Group(models.Model):

    name = models.CharField(max_length=200)

    description = models.TextField()

    members = models.ManyToManyField(settings.AUTH_USER_MODEL)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="created_groups"
    )

    def __str__(self):
        return self.name