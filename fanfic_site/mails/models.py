from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Mail(models.Model):
    """A model for creating user-to-user messages."""
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_mails')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_mails')
    subject = models.CharField(max_length=255)
    body = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.subject} from {self.sender.username} to {self.recipient.username}"