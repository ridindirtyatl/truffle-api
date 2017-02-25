from flask import Blueprint, jsonify, request



buses_api = Blueprint('buses_api', __name__)


@buses_api.route('/buses', methods=['GET'])
def buses_get():
    '''
    Get a list of all buses
    It is handler for GET /buses
    '''
    
    return jsonify()
