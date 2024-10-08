from App.models import Admin, User
from App.database import db

def create_admin(username, password, firstName, lastName, email):
    newAdmin = Admin(firstName=firstName, lastName=lastName, email=email,
        username=username, password=password)
    try:
        db.session.add(newAdmin)
        db.session.commit()
        return True, None
    except Exception as e:
        db.session.rollback()
        return False, e

def get_admin_by_username(username):
    admin = Admin.query.filter_by(username=username).first()
    return admin.get_json()

def get_admin_by_id(id):
    admin = Admin.query.filter_by(id=id).first()
    return admin.get_json()

def get_all_admins():
    admins = Admin.query.all()
    return admins #json

def get_all_admins_json():
    admins = Admin.query.all()
    if not admins:
        return []
    admins = [admin.get_json() for admin in admins]
    return admins

def update_admin_username(id, username):
    admin = get_admin_by_id(id)
    if admin:
        admin.username = username
        db.session.add(admin)
        return db.session.commit()
    return None

def is_admin(id):
    admin = Admin.query.filter_by(id=id).first()
    if not admin:
        return False
    return True