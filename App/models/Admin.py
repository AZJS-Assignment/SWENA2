from App.database import db
from .User import *
from .Company import *
from .Application import *
from .Job import *

class Admin(User):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    companyID = db.Column(db.Integer, db.ForeignKey('company.companyID'), nullable=True)
    
    def __init__(self, firstName, lastName, email, username, password):
        super().__init__(firstName, lastName, email, username, password)

    def get_json(self):
        person_data = super().get_json()
        return person_data