from flask import render_template
from flask import Blueprint

service_bp = Blueprint('service', __name__)

@service_bp.route('/service')
def service():
    data = {
        'headTitle': 'Service',
        'title': 'Service',
        'subTitle': 'Service',
    }
    return render_template("service/service.html",**data)

@service_bp.route('/service-details')
def serviceDetails():
    data = {
        'headTitle': 'Service Details',
        'breadcrumb': 'false',
    }
    return render_template("service/serviceDetails.html",**data)