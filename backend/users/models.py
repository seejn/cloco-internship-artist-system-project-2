from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

# Create your models here.
class CustomUserManager(BaseUserManager):
    
    def create(self, email, password, **kwargs):
        if not email:
            raise ValueError("Email is required")
        
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)

        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user


class AdminManager(models.Manager):

    def create(self, email, password, **kwargs):
        if not email:
            raise ValueError("Email is required")
        
        kwargs.setdefault("is_admin", True)

        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def get_queryset(self):
        return super().get_queryset().filter(is_admin=True)
    
class ArtistManager(models.Manager):

    def create(self, email, password, **kwargs):
        if not email:
            raise ValueError("Email is required")
        
        kwargs.setdefault("is_artist", True)

        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def get_queryset(self):
        return super().get_queryset().filter(is_artist=True)

class UserManager(models.Manager):

    def create(self, email, password, **kwargs):
        if not email:
            raise ValueError("Email is required")
        
        kwargs.setdefault("is_user", True)

        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def get_queryset(self):
        return super().get_queryset().filter(is_user=True)

class CustomUser(AbstractUser):
    username = None
    is_staff = None
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

    def create_admin(self, email, password, **kwargs):
        self.admin.create(email=email, password=password, **kwargs)
        return self

    def create_artist(self, email, password, **kwargs):
        self.artist.create(email=email, password=password, **kwargs)
        return self

    def create_user(self, email, password, **kwargs):
        self.user.create(email=email, password=password, **kwargs)
        return self

    def __str__(self):
        return self.email
