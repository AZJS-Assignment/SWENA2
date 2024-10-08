from App.models import *
from App.database import db

def create_application(applicantID, jobID, applicationDate):
    newApplication = Application(applicantID=applicantID, jobID=jobID, applicationDate=applicationDate)
    try:
        db.session.add(newApplication)
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        return False, e

def get_application_by_id(applicationID):
    application = Application.query.filter_by(applicationID=applicationID).first()
    return application #json

def get_applications_by_applicantID(applicantID):
    applications = Application.query.filter_by(id=applicantID).all()
    return applications

def get_applications_by_applicantID_json(applicantID):
    applications = Application.query.filter_by(id=applicantID).all()
    if not applications:
        return []
    applications = [application.get_json() for application in applications]
    return applications

def get_applications_by_jobID(jobID):
    applications = Application.query.filter_by(jobID=jobID).all()
    return applications

def get_applications_by_jobID_json(jobID):
    applications = Application.query.filter_by(jobID=jobID).all()
    if not applications:
        return []
    applications = [application.get_json() for application in applications]
    return applications
 
def get_all_applications():
    applications = Application.query.all()
    return applications

def get_all_applications_json():
    applications = Application.query.all()
    if not applications:
        return []
    applications = [application.get_json() for application in applications]