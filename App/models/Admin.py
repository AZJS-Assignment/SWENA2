from App.database import db
from .User import *
from .Company import *
from .Application import *
from .Job import *

class Admin(User):
    #companyID = db.Column(db.Integer, db.ForeignKey('company.companyID'), nullable=False)
    __mapper_args__ = {'polymorphic_identity': 'admin'}
    
    def __init__(self, firstName, lastName, email, username, password):
        super().__init__(firstName, lastName, email, username, password)

    def get_json(self):
        person_data = super().get_json()
        return person_data