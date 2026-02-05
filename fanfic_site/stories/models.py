from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse

from cloudinary_storage.storage import MediaCloudinaryStorage
from cloudinary.utils import cloudinary_url
from django.templatetags.static import static

User = get_user_model()

class Genre(models.Model):
    """Creates a table to house a set list of genres. Genres must be added by the admin, rather than the user."""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Story(models.Model):
    """The main model for creating stories."""
    STATUS_CHOICES = [
        ('draft', 'Draft (private)'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stories')
    summary = models.TextField(max_length=500)
    fandom = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='stories')

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )

    date_published = models.DateTimeField(default=timezone.now)
    cover_image = models.ImageField(
        upload_to='covers/',
        storage=MediaCloudinaryStorage(),
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('story-detail', kwargs={'pk': self.pk})
    
    def get_cover_image_url(self):
        if self.cover_image:
            return cloudinary_url(
                self.cover_image.name, width=140, height=210, crop="fill"
            )[0]
        else:
            return static('stories/default-cover.jpg')
    
class Chapter(models.Model):
    """Every story can have one or more chapters. This model creates the chapters and assigns them to a story.
    The 'number' refers to the chapter number. This can be changed by the user on the story_detail page"""
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
        return f"{self.story.title} - Chapter {self.number}"