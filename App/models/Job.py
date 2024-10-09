from App.database import db
from .Company import *

class Job(db.Model):
    jobID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    companyID = db.Column(db.Integer, db.ForeignKey('company.companyID'), nullable=False)
    salaryRange = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    applicationDeadline = db.Column(db.String(20), nullable=False)
    #company = db.relationship('Company', backref='jobs', lazy=True)

    def __init__(self, title, companyID, salaryRange, description, applicationDeadline):
        self.title = title
        self.companyID = companyID
        self.salaryRange = salaryRange
        self.description = description
        self.applicationDeadline = applicationDeadline

    def get_json(self):
        return {
            'jobID': self.jobID,
            'title': self.title,
            'companyID': self.companyID,
            'salaryRange': self.salaryRange,
            'description': self.description,
            'applicationDeadline': self.applicationDeadline
        }