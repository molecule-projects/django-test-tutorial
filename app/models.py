# app/models.py

from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=250)
    post = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
