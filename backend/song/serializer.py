def SongSerializer(obj):
    keys = ["id", "title", "release_data", "duration"]
    values = [obj.id, obj.title, obj.release_date, obj.duration]

    data = {k:v for k,v in zip(keys, values)}
    return data