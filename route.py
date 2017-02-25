from flask import Blueprint, jsonify, request



route_api = Blueprint('route_api', __name__)


@route_api.route('/route', methods=['GET'])
def route_get():
    '''
    Get a list of routes
    It is handler for GET /route
    '''
    
    return jsonify()


@route_api.route('/route/<id>', methods=['GET'])
def route_byId_get(id):
    '''
    Get information about a single route
    It is handler for GET /route/<id>
    '''
    
    return jsonify()
