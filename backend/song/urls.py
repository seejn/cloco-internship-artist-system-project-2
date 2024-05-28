from django.urls import path
from . import views

urlpatterns = [
    path("get_all_songs/", views.get_all_songs, name="get_all_songs"),
    path("<int:song_id>/", views.get_song, name="get_song"),
    path("<int:song_id>/update/", views.update_song, name="update_song"),
    path("<int:song_id>/delete/", views.delete_song, name="delete_song"),
]