from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = timezone.now
    completed = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='undefined')