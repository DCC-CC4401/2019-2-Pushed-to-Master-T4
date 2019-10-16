from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='profile_images', blank=True)

    @property
    def image_url(self):
        if self.image:
            return "static/img/" + self.image.url
        else:
            return "static/img/avatar.png"


class Activity(models.Model):
    name = models.CharField(blank=False, max_length = 30)
    description = models.CharField(blank=False, max_length=140)
    Choices = [('ST', 'Estudiar'), ('SL', 'Dormir'), ('SP', 'Deporte')]
    category = models.CharField(blank=False, max_length=100, choices=Choices)


class TipoActivity(models.Model):
    activity = models.ForeignKey(Activity, models.CASCADE)
    name = models.CharField(blank=False, max_length=30)


class NormalActivity(models.Model):
    activity = models.ForeignKey(Activity, models.CASCADE)
    startDate = models.DateTimeField(blank=False)
    endDate = models.DateTimeField(blank=False)


class FriendshipRelation(models.Model):
    user1 = models.ForeignKey(User, models.CASCADE, related_name="user1")
    user2 = models.ForeignKey(User, models.CASCADE, related_name="user2")
    Choices = [('F', 'Amigos'), ('W', 'Esperando confirmación'), ('P', 'Por aceptar confirmación')]
    state = models.CharField(blank=False, max_length=30, choices=Choices)


class ActivityBelongToUserRelation(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    activity = models.ForeignKey(Activity, models.CASCADE)