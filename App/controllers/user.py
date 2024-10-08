from App.models import *
from App.database import db

def get_all_users():
    users = User.query.all()
    return users

def get_all_users_json():
    users = User.query.all()
    return users