from App.models import *
from App.database import *

def create_company(companyName, adminID, location, industry):
    newCompany = Company(companyName=companyName, adminID=adminID, location=location, industry=industry)
    try:
        db.session.add(newCompany)
        db.session.commit()
        return True, None
    except Exception as e:
        db.session.rollback()
        return False, e

def get_company_by_id(companyID):
    company = Company.query.filter_by(companyID=companyID).first()
    return company.get_json()

def get_companies_by_adminID(adminID):
    companies = Company.query.filter_by(adminID=adminID).all()
    companies = [company.get_json() for company in companies]
    return companies

def get_all_companies():
    companies = Company.query.all()
    return companies

def get_all_companies_json():
    companies = Company.query.all()
    if not companies:
        return []
    companies = [company.get_json() for company in companies]
    return companies