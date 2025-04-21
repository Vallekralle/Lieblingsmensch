from django.db import models
from django.urls import reverse


class Message(models.Model):
    receiver = models.CharField(max_length=20, verbose_name ="Empfänger", help_text="z.B. Max Mustermann")
    content = models.TextField(max_length=100, verbose_name ="Nachricht", help_text="z.B. Ich mag an dir...")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse("home")

    def __str__(self):
        return f"{self.receiver} - {self.content}"