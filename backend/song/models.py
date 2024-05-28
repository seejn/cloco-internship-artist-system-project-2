from django.db import models
from users.models import CustomUser

# Create your models here.
class Song(models.Model):
    artist = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="song")
    title = models.CharField(max_length=100)
    release_date = models.DateField(null=True)
    duration = models.CharField(max_length=50, null=True)
    genre = models.CharField(max_length=100, null=True)
    image = models.CharField(default="https://via.placeholder.com/300", max_length=50)

    class Meta:
        db_table = "songs"

    def __str__(self):
        return self.title