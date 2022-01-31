from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(
        User, related_name='notes', on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[0:50]

    class Meta:
        ordering = ['created']
