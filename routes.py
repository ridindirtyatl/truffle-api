from flask import Blueprint, jsonify, request


routes_api = Blueprint('routes_api', __name__)


@routes_api.route('/v1/routes', methods=['GET'])
def routes_get():
    '''
    Get a list of routes
    It is handler for GET /routes
    '''

    return jsonify()
