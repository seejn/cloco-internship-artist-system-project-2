from django.shortcuts import render
from django.http import JsonResponse
from .serializers import SongSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from song.models import Song
from django.core.exceptions import ObjectDoesNotExist

import json


def get_all_songs(request):
    all_songs = Song.objects.all()

    if not all_songs:
        print("all_songs", all_songs)
        return JsonResponse({"message": "Songs not found"}, status=404)
        
    all_songs = [SongSerializer(song) for song in all_songs]

    return JsonResponse({"message": "All songs", "data": all_songs})

def get_song(request, song_id):
    try:
        song = Song.objects.get(pk=song_id)
    except ObjectDoesNotExist:
        return JsonResponse({"message": "Music not found"}, status=404)

    song = SongSerializer(song)

    return JsonResponse({"message": "Song", "data": song})

@csrf_exempt
def update_song(request, song_id):
    try:
        song = Song.objects.get(pk=song_id)
    except ObjectDoesNotExist:
        return JsonResponse({"message": "Music not found"}, status=404)
    
        
    updated_data = json.loads(request.body)
    song.__dict__.update(updated_data)
    song.save()
    updated_song = SongSerializer(song)
    
    return JsonResponse({"message": "Song Updated", "data": updated_song}, status=200)

@csrf_exempt
def delete_song(request, song_id):
    try:
        song = Song.objects.get(pk=song_id)
    except ObjectDoesNotExist:
        return JsonResponse({"message": "Music not found"}, status=404)

    song.delete()

    deleted_song = SongSerializer(song)
    return JsonResponse({"message": "Song Deleted", "data": deleted_song}, status=200)