from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
from .models import CustomUser, ArtistDetail
from .serializers import ArtistSerializer, UserSerializer
from song.serializer import SongSerializer


# CREATE USER METHODS

'''
REQUEST VALIDATION:
    - email and password field 
    - email and password must have value
'''


@csrf_exempt
def create_admin(request):
    print(request.POST)
    email = request.POST.get("email")
    password = request.POST.get("password")

    try:
        new_user = CustomUser.admin.create(email=email, password=password)
    except IntegrityError:
        return JsonResponse({"message": "Email already exists"}, status=400)
    except: 
        return JsonResponse({"message": "New Admin not Created"}, status=500)

    return JsonResponse({"message": "admin created", "data": {}}, status=200)

@csrf_exempt
def create_artist(request):
    print(bool(request.POST))
    email = request.POST.get("email")
    password = request.POST.get("password")

    try:
        new_artist = CustomUser.artist.create(email=email, password=password)
        detail = ArtistDetail.objects.create()
        detail.artist = new_artist
        detail.save()

    except IntegrityError:
        return JsonResponse({"message": "Email already exists"}, status=400)
    except: 
        return JsonResponse({"message": "New Artist not Created"}, status=500)

    new_artist = ArtistSerializer(new_artist)
    return JsonResponse({"message": "Artist created", "data": new_artist}, status=200)

@csrf_exempt
def create_user(request):
    print(bool(request.POST))
    email = request.POST.get("email")
    password = request.POST.get("password")

    try:
        new_user = CustomUser.user.create(email=email, password=password)
    except IntegrityError:
        return JsonResponse({"message": "Email already exists"}, status=400)
    except: 
        return JsonResponse({"message": "New User not Created"}, status=500)

    return JsonResponse({"message": "User created", "data": {}}, status=200)



# GET USER METHODS

def get_artist(request, artist_id):
    try:
        artist = CustomUser.artist.get(pk=artist_id)
        artist = ArtistSerializer(artist)
    except ObjectDoesNotExist:
        return JsonResponse({"message": "Artist not found"}, status=404)

    return JsonResponse({"message": "Artist Information", "data": artist}, status=200)

def get_all_artists(request):
    artists = CustomUser.artist.all()
    if not artists:
        return JsonResponse({"message": "No artists available"}, status=404)
        
    artists = [ArtistSerializer(artist) for artist in artists ]

    return JsonResponse({"message": "Artist Information", "data": artists}, status=200)

def get_user(request, user_id):
    try:
        user = CustomUser.user.get(pk=user_id)
        user = UserSerializer(user)
    except ObjectDoesNotExist:
        return JsonResponse({"message": "user not found"}, status=404)

    return JsonResponse({"message": "user Information", "data": user}, status=200)

def get_all_users(request):
    users = CustomUser.user.all()
    if not users:
        return JsonResponse({"message": "No users available"}, status=404)
        
    users = [UserSerializer(artist) for artist in users ]

    return JsonResponse({"message": "Artist Information", "data": users}, status=200)


# DELETE USER METHODS

@csrf_exempt
def delete_artist(request, artist_id):
    print("artist_id", artist_id)
    try:
        artist = CustomUser.artist.get(pk=artist_id)
        artist.is_deleted = True
        artist.save()
    except ObjectDoesNotExist:
        return JsonResponse({"message": "Artist not found"}, status=404)
    except:
        return JsonResponse({"message": "Artist not deleted"}, status=400)

    artist = ArtistSerializer(artist)
    return JsonResponse({"message": "Artist deleted", "data": artist}, status=200)

@csrf_exempt
def delete_user(request, user_id):
    print("user_id", user_id)
    try:
        user = CustomUser.user.get(pk=user_id)
        user.is_deleted = True
        user.save()
    except ObjectDoesNotExist:
        return JsonResponse({"message": "user not found"}, status=404)
    except:
        return JsonResponse({"message": "user not deleted"}, status=400)

    user = UserSerializer(user)
    return JsonResponse({"message": "user deleted", "data": user}, status=200)
    

# view artist's song
def get_songs(request, user_id):
    try:
        user = CustomUser.artist.get(pk=user_id)
    except ObjectDoesNotExist:
        return JsonResponse({"message": "user not found"}, status=404)
    
    songs = user.song.all()
    if not songs:
        return JsonResponse({"message": "Music not availabe"}, status=404)
        
    songs = [SongSerializer(song) for song in songs]
    return JsonResponse({"message": "Artist's songs", "data": songs}, status=200)

@csrf_exempt
def update_song(request, user_id, song_id):
    try:
        user = CustomUser.artist.get(pk=user_id)
    except ObjectDoesNotExist:
        return JsonResponse({"message": "user not found"}, status=404)
    
    song = user.song.get(pk=song_id)
    if not song:
        return JsonResponse({"message": "Music not availabe"}, status=404)
        
    updated_song = dict(request.POST)
    updated_song ={k: v[0] for k,v in updated_song.items()}
    print(updated_song)

    song.__dict__.update(updated_song)
    song.save()
    updated_song = SongSerializer(song)
    
    return JsonResponse({"message": "Song Updated", "data": updated_song}, status=200)

@csrf_exempt
def delete_song(request, user_id, song_id):
    try:
        user = CustomUser.artist.get(pk=user_id)
    except ObjectDoesNotExist:
        return JsonResponse({"message": "user not found"}, status=404)

    try:
        print(song_id)
        song = user.song.get(pk=song_id)
    except:
        return JsonResponse({"message": "Music not availabe"}, status=404)
    song.delete()

    deleted_song = SongSerializer(song)
    return JsonResponse({"message": "Song Deleted", "data": deleted_song}, status=200)