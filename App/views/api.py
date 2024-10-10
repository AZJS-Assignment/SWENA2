from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, set_access_cookies, unset_access_cookies, get_jwt_identity
from App.models import *
from App.controllers import *

api_views = Blueprint('api_views', __name__, template_folder="../templates")

# @api_views.route('/api/login', methods=['POST'])
# def user_login_api():
#     data = request.json
#     token = login(data['username'], data['password'])
#     if not token:
#         return jsonify(message='bad username or password given'), 401
#     response = jsonify(access_token=token) 
#     set_access_cookies(response, token)
#     return response


# Adds a new applicant
@api_views.route('/api/applicant', methods=['POST'])
def create_applicant_api():
    data = request.json
    if add_applicant(data['firstName'], data['lastName'], data['email'], data['username'], data['password'], data['resume']):
        return jsonify(message='applicant created'), 201
    else:
        return jsonify(message='applicant already exists'), 400

# Adds a new admin
@api_views.route('/api/admin', methods=['POST'])
def create_admin_api():
    data = request.json
    if add_admin(data['firstName'], data['lastName'], data['email'], data['username'], data['password']):
        return jsonify(message='admin created'), 201
    else:
        return jsonify(message='admin already exists'), 400

# Adds a new company
@api_views.route('/api/company', methods=['POST'])
@jwt_required()
def create_company_api():
    admin = get_admin_by_id(get_jwt_identity())
    if admin:
        data = request.json
        if add_company(data['companyName'],admin['id'],data['location'], data['industry']):
            return jsonify(message='company created'), 201
        else:
            return jsonify(message='company already exists'), 400
    else:
        return jsonify(message='not an admin')

# Adds a new job
@api_views.route('/api/job', methods=['POST'])
@jwt_required()
def create_job_api():
    if is_admin(get_jwt_identity()):
        data = request.json
        if create_job(data['title'], data['companyID'], data['salaryRange'], data['description'], data['applicationDeadline']):
            return jsonify(message="job created"), 201
        else:
            return jsonify(message="company does not exist"), 400
    else:
        return jsonify(message="NOT")

# Adds a new application
@api_views.route('/api/application', methods=['POST'])
@jwt_required()
def create_application_api():
    applicant = get_applicant_by_id(get_jwt_identity())
    if applicant:
        data = request.json
        if create_application(applicant['id'], data['jobID'], data['applicationDate']):
            return jsonify(message='application created'), 201
        else:
            return jsonify(message="application already exists"), 400
    else:
        return jsonify(message="not")

# View Applications for Job
@api_views.route('/api/getApplications/<int:job_id>', methods=['GET'])
@jwt_required()
def view_applications_api(job_id):
    if is_admin(get_jwt_identity()):
        job = get_job_by_id(job_id)
        if job:
            company = get_company_by_id(job['companyID'])
            if company['adminID'] == get_jwt_identity():
                applications = get_applications_by_jobID_json(job_id)
                return applications
            else:
                return jsonify(message='NOT THE ADMIN LISTING')
        else:
            return jsonify(message='NOT A JOB')
    else:
        return jsonify(message='NOT AN ADMIN')

# View Applicant's Applications
@api_views.route('/api/applications', methods=['GET'])
@jwt_required()
def view_applicant_applications_api():
    if is_applicant(get_jwt_identity()):
        applications = get_applications_by_applicantID_json(get_jwt_identity())
        return applications


# View All Jobs
@api_views.route('/api/jobs', methods=['GET'])
@jwt_required()
def view_jobs_command():
    jobs = get_all_jobs_json()
    return jobs

# View Admin's jobs
@api_views.route('/api/admin/jobs', methods=['GET'])
@jwt_required()
def view_admin_jobs_command():
    if is_admin(get_jwt_identity()):
        companies = get_companies_by_adminID(get_jwt_identity())
        jobs = [get_jobs_by_companyID(company['companyID']) for company in companies]
        return jobs