from App.database import db
from App.models import *
from App.controllers.commands import *

def initialize():
    db.drop_all()
    db.create_all()

    # Adding 5 admins, not linked to companies by default
    add_admin("Sophia", "Lewis", "sophia.lewis@example.com", "sophiaL", "SecurePass456")
    add_admin("Liam", "Robinson", "liam.robinson@example.com", "liamR", "StrongPass789")
    add_admin("Olivia", "Walker", "olivia.walker@example.com", "oliviaW", "Pass4321!")
    add_admin("Noah", "Hall", "noah.hall@example.com", "noahH", "SecurePass123")
    add_admin("Mia", "Young", "mia.young@example.com", "miaY", "Password987")

    # Adding 5 companies, linking to admins
    add_company("BrightTech", "San Francisco", "Technology")
    add_company("InnovateLLC", "Austin", "Consulting")
    add_company("FutureNet", "Boston", "Telecommunications")
    add_company("DataWorks", "Chicago", "Data Analytics")
    add_company("GreenEnergy", "Seattle", "Renewable Energy")

    # Adding 5 different jobs
    add_job("Software Engineer", 1, "$80,000 - $100,000", "Develop and maintain software applications.", "2024-12-31")
    add_job("Data Scientist", 2, "$90,000 - $120,000", "Analyze complex data to provide business insights.", "2024-11-30")
    add_job("Product Manager", 3, "$100,000 - $130,000", "Lead product development and manage teams.", "2024-10-15")
    add_job("UX Designer", 1, "$70,000 - $90,000", "Design user experiences and improve usability.", "2024-12-01")
    add_job("Systems Administrator", 4, "$60,000 - $85,000", "Manage IT infrastructure and system performance.", "2024-11-01")

    # Adding 10 applicants
    applicants = [
        ("Alice", "Johnson", "alice.johnson@example.com", "alicejohnson", "password123", "alice_resume.pdf"),
        ("Bob", "Smith", "bob.smith@example.com", "bobsmith", "password123", "bob_resume.pdf"),
        ("Charlie", "Brown", "charlie.brown@example.com", "charliebrown", "password123", "charlie_resume.pdf"),
        ("David", "Wilson", "david.wilson@example.com", "davidwilson", "password123", "david_resume.pdf"),
        ("Emma", "Davis", "emma.davis@example.com", "emmadavis", "password123", "emma_resume.pdf"),
        ("Frank", "Garcia", "frank.garcia@example.com", "frankgarcia", "password123", "frank_resume.pdf"),
        ("Grace", "Martinez", "grace.martinez@example.com", "gracemartinez", "password123", "grace_resume.pdf"),
        ("Henry", "Hernandez", "henry.hernandez@example.com", "henryhernandez", "password123", "henry_resume.pdf"),
        ("Ivy", "Clark", "ivy.clark@example.com", "ivyclark", "password123", "ivy_resume.pdf"),
        ("Jack", "Lopez", "jack.lopez@example.com", "jacklopez", "password123", "jack_resume.pdf"),
    ]
    for applicant in applicants:
        add_applicant(*applicant)
    
    # Adding 10 applications
    add_application(applicantID=6, jobID=1, applicationDate="2024-09-01")
    add_application(applicantID=7, jobID=1, applicationDate="2024-09-02")
    add_application(applicantID=8, jobID=2, applicationDate="2024-09-03")
    add_application(applicantID=9, jobID=2, applicationDate="2024-09-04")
    add_application(applicantID=10, jobID=3, applicationDate="2024-09-05")
    add_application(applicantID=11, jobID=3, applicationDate="2024-09-06")
    add_application(applicantID=12, jobID=4, applicationDate="2024-09-07")
    add_application(applicantID=13, jobID=4, applicationDate="2024-09-08")
    add_application(applicantID=14, jobID=5, applicationDate="2024-09-09")
    add_application(applicantID=15, jobID=5, applicationDate="2024-09-10")