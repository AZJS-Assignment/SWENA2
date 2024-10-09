from App.models import *
from App.database import *

def create_job(title, companyID, salaryRange, description, applicationDeadline):
    newJob = Job(
        title=title, 
        companyID=companyID, 
        salaryRange=salaryRange, 
        description=description, 
        applicationDeadline=applicationDeadline
    )
    try:
        db.session.add(newJob)
        db.session.commit()
        return True, None
    except Exception as e:
        db.session.rollback()
        return False, e

def get_job_by_id(jobID):
    job = Job.query.filter_by(jobID=jobID)
    return job #json

def get_all_jobs():
    jobs = Job.query.all()
    return jobs #json

def get_all_jobs_json():
    jobs = Job.query.all()
    if not jobs:
        return []
    jobs = [job.get_json() for job in jobs]
    return jobs

def delete_job(jobID):
    job = Job.query.filter_by(jobID=jobID).first()
    if job:
        db.session.delete(job)
        return db.session.commit()
    return None

def update_job_title(jobID, title):
    job = Job.query.filter_by(jobID=jobID).first()
    if job:
        job.title = title
        db.session.add(job)
        return db.session.commit()
    return None

def update_job_description(jobID, description):
    job = Job.query.filter_by(jobID=jobID).first()
    if job:
        job.description = description
        db.session.add(job)
        return db.session.commit()
    return None

def update_job_salary(jobID, salaryRange):
    job = Job.query.filter_by(jobID=jobID).first()
    if job:
        job.salaryRange = salaryRange
        db.session.add(job)
        return db.session.commit()
    return None