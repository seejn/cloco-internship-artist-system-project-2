def ArtistSerializer(obj):
    print("Artist Serializer", obj)
    keys = ['id', 'firstname', 'lastname', 'email', 'date_joined', 'last_login', 'stagename', 'dob', 'gender', 'nationality']
    values = [obj.id, obj.first_name, obj.last_name, obj.email, obj.date_joined, obj.last_login, obj.artistdetail.stagename, obj.artistdetail.dob, obj.artistdetail.gender, obj.artistdetail.nationality]

    data = {k: v for k,v in zip(keys, values)}
    return data


def UserSerializer(obj):
    print("User Serializer", obj)
    keys = ['id', 'firstname', 'lastname', 'email', 'date_joined', 'last_login']
    values = [obj.id, obj.first_name, obj.last_name, obj.email, obj.date_joined, obj.last_login]

    data = {k: v for k,v in zip(keys, values)}
    return data