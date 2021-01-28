from flask import jsonify, render_template, request
from werkzeug.http import HTTP_STATUS_CODES

from server import db
from server.api import bp


def api_error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response


@bp.app_errorhandler(404)
def not_found_error(error):
    return api_error_response(404)


@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return api_error_response(500)