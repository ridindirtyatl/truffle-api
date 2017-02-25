from flask import Blueprint, jsonify, request



routeid_api = Blueprint('routeid_api', __name__)


@routeid_api.route('/route/<id>', methods=['GET'])
def routeid_get(id):
    '''
    Get information about a single route
    It is handler for GET /route/<id>
    '''
    
    return jsonify()
