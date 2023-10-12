# WEBUI/models.py
from django.db import models

class ChatMessage(models.Model):
    content = models.TextField()
    is_user = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'WEBUI'
