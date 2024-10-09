from App.database import db
from .User import User
from .Job import *
from .Application import *

class Applicant(User):
    resume = db.Column(db.String(1024), nullable=True)
    __mapper_args__ = {'polymorphic_identity': 'applicant'}

    def __init__(self, firstName, lastName, email, username, password, resume):
        super().__init__(firstName=firstName, lastName=lastName, email=email, username=username, password=password)
        self.resume = resume

    def get_json(self):
        person_data = super().get_json()
        person_data['resume'] = self.resume
        return person_data