from App.database import db
from .User import *
from .Company import *
from .Application import *
from .Job import *

class Admin(User):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    companyID = db.Column(db.Integer, db.ForeignKey('company.companyID'), nullable=False)
    
    def __init__(self, firstName, lastName, email, username, password, companyID):
        super().__init__(firstName, lastName, email, username, password)
        self.companyID = companyID

    def get_json(self):
        person_data = super().get_json()
        person_data['companyID'] = self.companyID
        return person_data