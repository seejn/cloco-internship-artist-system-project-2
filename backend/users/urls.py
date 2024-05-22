from django.urls import path
from . import views

urlpatterns = [
    path('create_admin/', views.create_admin, name='create_admin'),
    path('create_artist/', views.create_artist, name='create_artist'),
    path('create_user/', views.create_user, name='create_user'),

    path('get_artist/<int:artist_id>/', views.get_artist, name='get_artist'),
    path('get_all_artists/', views.get_all_artists, name='get_all_artists'),
    path('get_user/<int:user_id>/', views.get_user, name='get_user'),
    path('get_all_users/', views.get_all_users, name='get_all_users'),
    
    path('delete_artist/<int:artist_id>/', views.delete_artist, name='delete_artist'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),

]