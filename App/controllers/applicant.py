from App.models import Applicant
from App.database import db

def create_applicant(username, password, firstName, lastName, email, resume):
    newApplicant = Applicant(firstName=firstName, lastName=lastName, email=email,
        username=username, password=password, resume=resume)
    try:
        db.session.add(newApplicant)
        db.session.commit()
        return True, None
    
    except Exception as e:
        db.session.rollback()
        return False, e

def get_applicant_by_username(username):
    applicant = Applicant.query.filter_by(username=username).first()
    return applicant

def get_applicant_by_id(id):
    applicant = Applicant.query.filter_by(id=id).first()
    return applicant.get_json()

def get_all_applicants():
    applicants = Applicant.query.all()
    return applicants

def get_all_applicants_json():
    applicants = Applicant.query.all()
    for applicant in applicants:
        if not applicant:
            return []
        applicants = [applicant.get_json() for applicant in applicants]
        return applicants

def update_applicant_username(id, username):
    applicant = Applicant.query.filter_by(id=id).first()
    if applicant:
        applicant.username = username
        db.session.add(applicant)
        return db.session.commit()
    return None

def update_applicant_resume(id, resume):
    applicant = Applicant.query.filter_by(id=id).first()
    if applicant:
        applicant.resume = resume
        db.session.add(applicant)
        return db.session.commit()
    return None

def is_applicant(id):
    applicant = Applicant.query.filter_by(id=id).first()
    if applicant:
        return True
    return False