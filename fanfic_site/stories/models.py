from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class Story(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    summary = models.CharField(max_length=500)
    fandom = models.CharField(max_length=100)
    rating = models.CharField(max_length=30)
    co_author = models.CharField(max_length=40)
    status = models.CharField(max_length=30)
    content = models.TextField()
    date_published = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title

