from django.db import models
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password, **kwargs):
        if not email:
            raise ValueError("Email is required")
        
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_staff", True)

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
        return super().get_queryset().filter(is_admin=True).filter(is_deleted=False)

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
        return super().get_queryset().filter(is_artist=True).filter(is_deleted=False)


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
        return super().get_queryset().filter(is_user=True).filter(is_deleted=False)