from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    image = models.ImageField(upload_to='profile_images', blank=True)
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()     
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