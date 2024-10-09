from App.database import db
from .User import User
from .Job import *
from .Application import *

class Applicant(User):
    id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    resume = db.Column(db.String(1024), nullable=True)
    applications = db.relationship('Application', backref='applicant', lazy=True)

    def __init__(self, firstName, lastName, email, username, password, resume):
        super().__init__(firstName=firstName, lastName=lastName, email=email, username=username, password=password)
        self.resume = resume

    def get_json(self):
        person_data = super().get_json()
        person_data['resume'] = self.resume
        return person_data