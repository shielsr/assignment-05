from django.db.models.signals import (
    post_save,
)  # This gets fired whenever an instance is saved
from django.contrib.auth.models import User  # The user model will be the sender
from django.dispatch import receiver  # This lets us receive the signal
from .models import Profile  # We'll create a new instance of this model Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance
        )  # create and save to the db the new profile instance
