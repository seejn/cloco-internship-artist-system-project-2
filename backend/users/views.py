from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password

# Create your views here.
from Token.models import Token
from .models import CustomUser, ArtistDetail
from .serializers import ArtistSerializer, UserSerializer
from decorators.decorators import api_view, login_required, check_auth_token
from song.serializers import SongSerializer

import json

# CREATE USER METHODS

'''
REQUEST VALIDATION:
    - email and password field 
    - email and password must have value
'''

def authenticate(email, password):
    print("inside authenticate")
    try:
        user = CustomUser.objects.get(email=email)
    except:
        return False

    hashed_password = user.password
    print("user", password)
    print("user", hashed_password)

    if not check_password(password, hashed_password): 
        return False

    return user

    

@csrf_exempt
def authenticate_user(request):
    # CHECK FOR BEARER AUTH TOKEN
    if request.headers.get('Authorization'):
        user = check_auth_token(request)
        if user:
            extra_fields = {
                "is_artist": user.is_artist,
                "is_admin": user.is_admin,
                "is_user": user.is_user,
            }
            user = UserSerializer(user) 
            user = {**user, **extra_fields}
            return JsonResponse({"message": "Authentication with token", "data": user}, status=200)

    if not bool(request.body):
        return JsonResponse({"message": "Required fields not Found"}, status=400)

    data = json.loads(request.body)

    email = data.get("email")
    password = data.get("password")

    user = authenticate(email, password)
    print("user", user)

    if not user:
        return JsonResponse({"message": "email or password is incorrect"}, status=401)

    try:
        token = user.create_token(t_type="access")
    except IntegrityError: 
        return JsonResponse({"message": "Token already exists"}, status=400)

    user = UserSerializer(user)

    response = JsonResponse({"message": "login success", "access": token, "data": user}, status=200)
    return response


@csrf_exempt
@login_required
def sign_out(request):
    token = request.headers["Authorization"].split(" ")[1]
    Token.objects.get(token=token).delete()
    return JsonResponse({"message": "You've signed out"}, status=200)


@csrf_exempt
def register_user(request):
    if not bool(request.body):
        return JsonResponse({"message": "Required fields not Found"}, status=400)
    
    
    data = json.loads(request.body)
    keys = [key for key in data.keys()]
    required_fields = ["email", "password"]
    for field in required_fields:
        if field not in keys:
            return JsonResponse({"message": "Required fields not Found"}, status=400)
            
    email = data.get("email")
    password = data.get("password")

    try:
        user = CustomUser.user.create(email=email, password=password)
        user = UserSerializer(user)
    except IntegrityError:
        return JsonResponse({"message": "User Already Exists"}, status=403)

    return JsonResponse({"message": "New user created", "data": user}, status=201)


@csrf_exempt
@api_view(["POST"])
def create_admin(request):
    print(request.body)
    data = json.loads(request.body)
    email = data.get("email")
    password = data.get("password")

    try:
        new_user = CustomUser.admin.create(email=email, password=password)
    except IntegrityError:
        return JsonResponse({"message": "Email already exists"}, status=400)
    except: 
        return JsonResponse({"message": "New Admin not Created"}, status=500)

    return JsonResponse({"message": "admin created", "data": {}}, status=200)

@csrf_exempt
@api_view(["POST"])
@login_required
def create_artist(request):
    print(request.body)
    data = json.loads(request.body)
    email = data.get("email")
    password = data.get("password")

    try:
        new_artist = CustomUser.artist.create(email=email, password=password)
        new_artist.__dict__.update(data)
        new_artist.save()
        print(new_artist)
        detail = ArtistDetail.objects.create()
        detail.artist = new_artist
        detail.save()

    except IntegrityError:
        return JsonResponse({"message": "Email already exists"}, status=400)
    except: 
        return JsonResponse({"message": "New Artist not Created"}, status=500)

    new_artist = ArtistSerializer(new_artist)
    return JsonResponse({"message": "Artist created Successfully", "data": new_artist}, status=200)

@csrf_exempt
@api_view(["POST"])
def create_user(request):
    print(request.body)
    data = json.loads(request.body)
    email = data.get("email")
    password = data.get("password")

    try:
        new_user = CustomUser.user.create(email=email, password=password)
    except IntegrityError:
        return JsonResponse({"message": "Email already exists"}, status=400)
    except: 
        return JsonResponse({"message": "New User not Created"}, status=500)

    return JsonResponse({"message": "New User created", "data": {}}, status=200)



# GET USER METHODS

@api_view(["GET"])
def get_artist(request, artist_id):
    try:
        artist = CustomUser.artist.get(pk=artist_id)
        artist = ArtistSerializer(artist)
    except ObjectDoesNotExist:
        return JsonResponse({"message": "Artist not found"}, status=404)

    return JsonResponse({"message": "Artist Information", "data": artist}, status=200)

@api_view(["GET"])
def get_all_artists(request):
    print("cleared login required")
    artists = CustomUser.artist.all()
    if not artists:
        return JsonResponse({"message": "No artists available"}, status=404)
        
    artists = [ArtistSerializer(artist) for artist in artists ]

    return JsonResponse({"message": "Artist Information", "data": artists}, status=200)

@api_view(["GET"])
def get_user(request, user_id):
    try:
        user = CustomUser.user.get(pk=user_id)
        user = UserSerializer(user)
    except ObjectDoesNotExist:
        return JsonResponse({"message": "user not found"}, status=404)

    return JsonResponse({"message": "user Information", "data": user}, status=200)

@api_view(["GET"])
def get_all_users(request):
    users = CustomUser.user.all()
    if not users:
        return JsonResponse({"message": "No users available"}, status=404)
        
    users = [UserSerializer(artist) for artist in users ]

    return JsonResponse({"message": "Artist Information", "data": users}, status=200)

# UPDATE USER METHODS

@csrf_exempt
@api_view(["PUT"])
@login_required
def update_artist(request, artist_id):
    try:
        artist = CustomUser.artist.get(pk=artist_id)
    except ObjectDoesNotExist:
        return JsonResponse({"message": "user not found"}, status=404)
    
    updated_data = json.loads(request.body)
    print("updated_data", updated_data)
    print("artist", artist)

    artist.__dict__.update(updated_data)
    artist.save()

    artist.artistdetail.__dict__.update(updated_data)
    artist.artistdetail.save()

    updated_artist = ArtistSerializer(artist)
    print(updated_artist)
    return JsonResponse({"message": "Artist Updated Successfully", "data": updated_artist}, status=200)

# DELETE USER METHODS

@csrf_exempt
@api_view(["DELETE"])
@login_required
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
    return JsonResponse({"message": "Artist deleted successfully", "data": artist}, status=200)

@csrf_exempt
@api_view(["DELETE"])
@login_required
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
    return JsonResponse({"message": "User deleted Successfully", "data": user}, status=200)
    

# view artist's song
@api_view(["GET"])
@login_required
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
@api_view(["POST"])
@login_required
def create_song(request, user_id, **kwargs):
    try:
        user = CustomUser.artist.get(pk=user_id)
    except ObjectDoesNotExist:
        return JsonResponse({"message": "user not found"}, status=404)

    data = json.loads(request.body)
    print(data)

    new_song = user.song.create(**data, **kwargs)
    new_song = SongSerializer(new_song)

    return JsonResponse({"message": "New Song Creatd", "data": new_song}, status=200)
    

