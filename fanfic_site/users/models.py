from django.db import models
from django.contrib.auth import get_user_model

from cloudinary_storage.storage import MediaCloudinaryStorage
from cloudinary.utils import cloudinary_url
from django.templatetags.static import static

User = get_user_model()

class Profile(models.Model):
    """The standard Profile model, allowing users to add a profile image etc."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='profile_pics',
        storage=MediaCloudinaryStorage(),
        null=True, # a missing profile image is handled by get_image_url
    )

    def get_image_url(self):
        if self.image: # Generate a Cloudinary thumbnail URL
            return cloudinary_url(
                self.image.name, width=300, height=300, crop="lfill"
            )[0]
        else: # Fallback to static default image
            return static('users/default-profile.png')
        
    def __str__(self):
        return self.user.username