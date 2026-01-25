from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Story(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft (private)'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stories')
    summary = models.TextField(max_length=500)
    fandom = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='stories')
    rating = models.CharField(max_length=30)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )

    date_published = models.DateTimeField(default=timezone.now)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('story-detail', kwargs={'pk': self.pk})
    
class Chapter(models.Model):
    story = models.ForeignKey(
        Story,
        related_name='chapters',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    number = models.PositiveIntegerField()
    date_published = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['number']
        unique_together = ('story', 'number')

    def __str__(self):
        return f"{self.story.title} – Chapter {self.number}"
    
    
