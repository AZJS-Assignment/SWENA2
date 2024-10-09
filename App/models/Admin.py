from App.database import db
from .User import *
from .Company import *
from .Application import *
from .Job import *

class Admin(User):

    def __init__(self, firstName, lastName, email, username, password):
        super().__init__(firstName, lastName, email, username, password)

    def get_json(self):
        person_data = super().get_json()
        return person_data
    
    def __repr__(self):
        return f'<Admin {self.username}>'
    
    def createJob(self, title, salaryRange, description, applicationDeadline):
        """Create a job by calling Job's createJob method"""
        new_job = Job(title, salaryRange, description, applicationDeadline)
        return new_job.createJob()

    def updateJob(self, jobID, new_title, new_salaryRange, new_description, new_applicationDeadline):
        """Update a job by calling Job's updateJob method"""
        job = Job.query.get(jobID)
        if job:
            return job.updateJob(new_title, new_salaryRange, new_description, new_applicationDeadline)
        return False

    def deleteJob(self, jobID):
        """Delete a job by calling Job's deleteJob method"""
        job = Job.query.get(jobID)
        if job:
            return job.deleteJob()
        return False
