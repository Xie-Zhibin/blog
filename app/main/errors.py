"""Error handlers."""
from flask import jsonify
from app.main import main


@main.app_errorhandler(404)
def not_found(e):
    """Not found."""
    error = {
        'msg': 'not found',
        'status': 0
    }
    return jsonify(error), 404


@main.app_errorhandler(500)
def internal_error(e):
    """Internal error."""
    error = {
        'msg': 'internal server error',
        'status': 0
    }
    return jsonify(error), 500
