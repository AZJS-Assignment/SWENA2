import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup
from App.controllers import initialize
from App.controllers.commands import *
from App.main import *
from App.models import *
from App.controllers import *
from App.database import db
import random

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

'''
# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli


#Test Commands


test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)

'''

'''
Hire Hub Commands
'''

hirehub = AppGroup('hirehub', help="Utilizes different features of the HireHub")

@hirehub.command('all_tables')
def display_all_tables_command():
    """Display all tables and their data."""
    view_tables()

# works
@hirehub.command("add_applicant")
@click.argument("first_name")  
@click.argument("last_name") 
@click.argument("email")
@click.argument("username")
@click.argument("password")
@click.argument("resume")
def add_applicant_command(first_name, last_name, email, username, password, resume):
    """Add an applicant to the database."""
    add_applicant(first_name, last_name, email, username, password, resume)

# works
@hirehub.command("add_company")
@click.argument("company_name")
@click.argument("admin_id")
@click.argument("location")
@click.argument("industry")
def add_company_command(company_name, admin_id, location, industry):
    """Add a company to the database."""
    add_company(company_name, admin_id, location, industry)

# works
@hirehub.command("add_job")
@click.argument("title")
@click.argument("companyid")
@click.argument("salaryrange")
@click.argument("description")
@click.argument("applicationdeadline")
def add_job_command(title, companyid, salaryrange, description, applicationdeadline):
    """Add a job to the database."""
    add_job(title, companyid, salaryrange, description, applicationdeadline)

# works
@hirehub.command("add_application")
@click.argument("applicantid")
@click.argument("jobid")
@click.argument("applicationdate")
def add_application_command(applicantid, jobid, applicationdate):
    """Add an application to the database."""
    add_application(applicantid, jobid, applicationdate)

# works
@hirehub.command("add_admin")
@click.argument("firstname")
@click.argument("lastname")
@click.argument("email")
@click.argument("username")
@click.argument("password")
def add_admin_command(firstname, lastname, email, username, password):
    add_admin(firstname, lastname, email, username, password)

# formatting output
@hirehub.command("view_all_applicants")
def view_applicants_command():
    """Display all applicants in the database."""
    view_all_applicants()

# formatting output
@hirehub.command("view_companies")
def view_companies_command():
    """Display all companies in the database."""
    view_all_companies()

# formatting output
@hirehub.command("view_applications")
def view_applications_command():
    """Display all applications in the database."""
    view_all_applications()

# formatting output
@hirehub.command("view_jobs")
def view_jobs_command():
    """Display all jobs in the database."""
    view_all_jobs()

#needs work add context
@hirehub.command("view_applicants")
@click.argument("job_id")
def view_applicants_by_job_command(job_id):
    """View all applicants for a specific job."""
    view_applications(job_id)

app.cli.add_command(hirehub)