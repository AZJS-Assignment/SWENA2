from App.models import *

def get_all_users():
    users = User.query.all()
    return users

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users