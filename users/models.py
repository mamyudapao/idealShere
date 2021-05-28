from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

class CustomUser(AbstractUser):
    skill = models.CharField(max_length=200, null=True, blank=True)
    introduction = models.CharField(max_length=300,  null=True, blank=True)
    image = models.ImageField(upload_to='users/', null=True, blank=True, default='api/posts/sample.jpg')
    projects = models.ManyToManyField('posts.Post')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)