from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager, AdminManager, ArtistManager, UserManager
import secrets
# Create your models here.

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(max_length=50, unique=True)
    image = models.CharField(default="https://via.placeholder.com/150", max_length=50)
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

    def create_token(self, t_type):
        token = secrets.token_hex(32)
        self.token.create(t_type=t_type, token=token)
        return token

class ArtistDetail(models.Model):
    artist = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    stagename = models.CharField(null=True, unique=True, max_length=50)
    biography = models.TextField(null=True, max_length=250)
    dob = models.DateField(null=True)
    gender = models.CharField(default="male", max_length=10)
    nationality = models.CharField(null=True, max_length=50)
    twitter_link = models.CharField(null=True, max_length=100)
    facebook_link = models.CharField(null=True, max_length=100)
    instagram_link = models.CharField(null=True, max_length=100)

    class Meta:
        db_table = "artist_details"

    def __str__(self):
        return "ArtistDetail"