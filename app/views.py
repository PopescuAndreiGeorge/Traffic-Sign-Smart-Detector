from flask import Blueprint, render_template, request
from .tools.sparql_queries import *

main_bp = Blueprint('main', __name__)

# @main_bp.route('/traffic_sign/api_test', methods=['GET'])
# def traffic_sign():
#     results = test_query()
#     return results

# @main_bp.route('/traffic_sign/<sign_name>', methods=['GET'])
# def traffic_sign_name(sign_name):
#     # no_passing -> NoPassing

#     results = get_sign_info(sign_name)
#     return results