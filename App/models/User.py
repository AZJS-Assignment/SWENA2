from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from .Job import *

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    type = db.Column(db.String(50))
    __mapper_args__ = {'polymorphic_identity': 'user', 'polymorphic_on': type}
    applications = db.relationship('Application', backref='user', lazy=True)
    companyRelation = db.relationship('Company', backref='user', lazy=True)

    def __init__(self, firstName, lastName, email, username, password):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.username = username
        self.set_password(password)

    def get_json(self):
        return {
            'id': self.id,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'email': self.email,
            'username': self.username,
            'type': self.type
        }
    
    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)