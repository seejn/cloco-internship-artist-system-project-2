from users.serializers  import ArtistSerializer
def SongSerializer(obj):
    keys = ["id", "title", "release_date", "duration", "genre" , "duration" , "artist"]
    values = [obj.id, obj.title, obj.release_date, obj.duration, obj.genre, obj.duration, ArtistSerializer(obj.artist)]

    data = {k:v for k,v in zip(keys, values)}
    return data