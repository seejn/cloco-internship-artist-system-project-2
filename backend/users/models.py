from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager, AdminManager, ArtistManager, UserManager

# Create your models here.

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(max_length=50, unique=True)
    is_deleted = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_artist = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    

    objects = CustomUserManager()
    admin = AdminManager()
    artist = ArtistManager()
    user = UserManager()

    class Meta:
        db_table = "c_users"

    def __str__(self):
        return self.email

    def set_artist_detail(self, artist, stagename, **kwargs):
        detail = ArtistDetail.objects.create(stagename=stagename, **kwargs)
        detail.artist = artist
        detail.save()

class ArtistDetail(models.Model):
    artist = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    stagename = models.CharField(null=True, unique=True, max_length=50)
    dob = models.DateField(null=True)
    gender = models.CharField(default="male", max_length=10)
    nationality = models.CharField(null=True, max_length=50)

    class Meta:
        db_table = "artist_details"

    def __str__(self):
        return "ArtistDetail"