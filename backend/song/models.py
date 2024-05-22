from django.db import models

# Create your models here.
class Song(models.Model):
    artist = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="song")
    title = models.CharField(max_length=100)
    release_date = models.DateField(null=True)
    duration = models.CharField(max_length=50, null=True)