from django.db import models

class Message(models.Model):
    receiver = models.CharField(max_length=20, verbose_name ="Empfänger", help_text="z.B. Max Mustermann")
    content = models.TextField(max_length=100, verbose_name ="Nachricht", help_text="z.B. Ich mag an dir...")
    created_at = models.DateTimeField(auto_now_add=True)
