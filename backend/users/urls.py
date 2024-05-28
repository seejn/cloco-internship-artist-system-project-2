from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_user, name="register_user"),
    path('user/', views.authenticate_user, name="authenticate_user"),
    path('sign_out/', views.sign_out, name="sign_out"),

    path('create_admin/', views.create_admin, name='create_admin'),
    path('create_artist/', views.create_artist, name='create_artist'),
    path('create_user/', views.create_user, name='create_user'),

    path('get_artist/<int:artist_id>/', views.get_artist, name='get_artist'),
    path('get_all_artists/', views.get_all_artists, name='get_all_artists'),
    path('get_user/<int:user_id>/', views.get_user, name='get_user'),
    path('get_all_users/', views.get_all_users, name='get_all_users'),
    
    path('update_artist/<int:artist_id>/', views.update_artist, name='update_artist'),

    path('delete_artist/<int:artist_id>/', views.delete_artist, name='delete_artist'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),

    path("<int:user_id>/get_songs/", views.get_songs, name="view_user_songs"),
    path("<int:user_id>/create_song/", views.create_song, name="create_user_songs="),
    # path("<int:user_id>/update_song/<int:song_id>/", views.update_song, name="update_user_song"),
    # path("<int:user_id>/delete_song/<int:song_id>/", views.delete_song, name="delete_user_song"),

]
