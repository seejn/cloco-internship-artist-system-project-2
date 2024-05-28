def ArtistSerializer(obj):
    fullname = f"{obj.first_name} {obj.last_name}"
    # print("Artist Serializer", obj)
    keys = ['id', 'fullname', 'email', 'date_joined', 'last_login', 'stagename', 'dob', 'gender', 'nationality', 'biography', 'facebook_link', 'twitter_link', 'instagram_link', "songs_count"]
    values = [obj.id, fullname, obj.email, obj.date_joined, obj.last_login, obj.artistdetail.stagename, obj.artistdetail.dob, obj.artistdetail.gender, obj.artistdetail.nationality, obj.artistdetail.biography, obj.artistdetail.facebook_link, obj.artistdetail.twitter_link, obj.artistdetail.instagram_link, len(obj.song.all())]

    data = {k: v for k,v in zip(keys, values)}
    return data


def UserSerializer(obj):
    # print("User Serializer", obj)
    keys = ['id', 'firstname', 'lastname', 'email', 'date_joined', 'last_login', 'is_artist', 'is_admin']
    values = [obj.id, obj.first_name, obj.last_name, obj.email, obj.date_joined, obj.last_login, obj.is_artist, obj.is_admin]

    data = {k: v for k,v in zip(keys, values)}
    return data

