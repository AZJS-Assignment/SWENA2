from App.models import *
from App.database import *

def create_company(companyName, adminUserName, location, industry):
    newCompany = Company(companyName=companyName, adminUserName=adminUserName, location=location, industry=industry)
    try:
        db.session.add(newCompany)
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        return False, e

def get_company_by_id(companyID):
    company = Company.query.filter_by(companyID=companyID).first()
    return company #json

def get_all_companies():
    companies = Company.query.all()
    return companies

def get_all_companies_json():
    companies = Company.query.all()
    if not companies:
        return []
    companies = [company.get_json() for company in companies]
    return companies