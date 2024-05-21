from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    username = None
    is_staff = None
    email = models.EmailField(max_length=50, unique=True)
    is_admin = models.PositiveIntegerField(default=0)
    is_artist = models.PositiveIntegerField(default=0)
    is_user = models.PositiveIntegerField(default=0)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def create_admin(self, email, password, **kwargs):
        self.objects.create(email=email, password=password, is_admin=1, **kwargs)
        self.save()
        return self

    def create_artist(self, email, password, **kwargs):
        self.objects.create(email=email, password=password, is_artist=1, **kwargs)
        self.save()
        return self

    def create_user(self, email, password, **kwargs):
        self.objects.create(email=email, password=password, is_user=1, **kwargs)
        self.save()
        return self

    def __str__(self):
        return self.email

    class Meta:
        db_table = "c_users"