from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    fecha = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_images',blank=True)

    @property
    def image_url(self):
        if self.image:
            return "static/img/"+self.image.url
        else:
            return "static/img/avatar.png"