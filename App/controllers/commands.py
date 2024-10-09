from App.controllers import *
from App.models import *
from App.database import db

# Command 1 - Create Applicant
def add_applicant(firstName, lastName, email, username, password, resume):
    result, err = create_applicant(username, password, firstName, lastName, email, resume)
    if result:
        print(f"{username} created successfully...")
    else:
        print(f"Error: {err}")

#Command 2 - Create Admin
def add_admin(firstName, lastName, email, username, password, companyID):
    result, err = create_admin(username, password, firstName, lastName, email, companyID)
    if result:
        print(f"{username} created successfully...")
    else:
        print(f"Error: {err}")

# Command 3 - Create Company
def add_company(companyName, location, industry):
    result, err = create_company(companyName, location, industry)
    if result:
        print(f"{companyName} created successfully...")
    else:
        print(f"Error: {err}")

# Command 4 - Create Job
def add_job(title, companyID, salaryRange, description, applicationDeadline):
    result, err = create_job(title, companyID, salaryRange, description, applicationDeadline)
    if result:
        print(f"{title} - ${salaryRange} created successfully...")
    else:
        print(f"Error: {err}")

# Command 5 - Create Application
def add_application(applicantID, jobID, applicationDate):
    result, err = create_application(applicantID, jobID, applicationDate)
    if result:
        print("Application created successfully...")
    else:
        print(f"Error: {err}")

# Command 6 - View All Applicants
def view_all_applicants():
    applicants = get_all_applicants_json()
    print(f"{applicants}")

# Command 7 - View All Companies
def view_all_companies():
    companies = get_all_companies_json()
    print(f"{companies}")

# Command 8 - View All Jobs
def view_all_jobs():
    jobs = get_all_jobs_json()
    print(f"{jobs}")

# Command 9 - View All Applications
def view_all_applications():
    applications = get_all_applications_json()
    print(f"{applications}")

# Command 10 - View Applications for a Job
def view_applications(jobID):
    applications = get_applications_by_jobID_json(jobID)
    print(f"{applications}")

# Command 11 - View All Tables
def view_tables():
    companies = get_all_companies_json()
    applicants = get_all_applicants_json()
    applications = get_all_applications_json()
    jobs = get_all_jobs_json()
    admins = get_all_admins_json()
    applicants = get_all_applicants_json()
    
    for company in companies:
        print(f"{company}")
    for job in jobs:
        print(f"{job}")
    for admin in admins:
        print(f"{admin}")
    for applicant in applicants:
        print(f"{applicant}")
    for application in applications:
        print(f"{application}")