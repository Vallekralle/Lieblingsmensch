from django.db import models

class Message(models.Model):
    receiver = models.CharField(max_length=20)
    content = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
