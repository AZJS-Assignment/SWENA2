from App.models import Admin
from App.database import db

def create_admin(username, password, firstName, lastName, email, companyID):
    newAdmin = Admin(firstName=firstName, lastName=lastName, email=email,
        username=username, password=password, companyID=companyID)
    try:
        db.session.add(newAdmin)
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        return False, e

def get_admin_by_username(username):
    admin = Admin.query.filter_by(username=username).first()
    return admin #json

def get_admin_by_id(id):
    admin = Admin.query.filter_by(id=id).first()
    return admin #json

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