from App.database import db

class Company(db.Model):
    companyID = db.Column(db.Integer, primary_key=True)
    adminID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    companyName = db.Column(db.String(120), unique=True, nullable=False)
    location = db.Column(db.String(120), nullable=False)
    industry = db.Column(db.String(120), nullable=False)

    def __init__(self, companyName, adminID, location, industry):
        self.companyName = companyName
        self.adminID = adminID
        self.location = location
        self.industry = industry
    
    def get_json(self):
        return {
            'companyID': self.companyID,
            'companyName': self.companyName,
            'adminID': self.adminID,
            'location': self.location,
            'industry': self.industry
        }