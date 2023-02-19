def user_serializer(user) -> dict:
    return {
        'id':str(user["_id"]),
        'name':user["name"],
        'role':user["role"]
       
    }


def users_serializer(users) -> list:
    return [user_serializer(user) for user in users] 
