from django.db import models
from user_service.models import User

class HashTag(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Discussion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='discussions/', null=True, blank=True)
    hashtags = models.ManyToManyField(HashTag)
    created_on = models.DateTimeField(auto_now_add=True)
