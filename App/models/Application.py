from App.database import db

class Application(db.Model):
    applicationID = db.Column(db.Integer, primary_key=True)
    applicantID = db.Column(db.Integer, db.ForeignKey('applicant.id'), nullable=False)
    jobID = db.Column(db.Integer, db.ForeignKey('job.jobID'), nullable=False)
    applicationDate = db.Column(db.String(20), nullable=False)

    def __init__(self, applicantID, jobID, applicationDate):
        self.applicantID = applicantID
        self.jobID = jobID
        self.applicationDate = applicationDate

    def get_json(self):
        return {
            'applicationID': self.applicationID,
            'applicantID': self.applicantID,
            'jobID': self.jobID,
            'applicationDate': self.applicationDate
        }