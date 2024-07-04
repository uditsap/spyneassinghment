from django.db import models
from user_service.models import User

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
