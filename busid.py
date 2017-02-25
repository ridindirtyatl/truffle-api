from flask import Blueprint, jsonify, request


busid_api = Blueprint('busid_api', __name__)


@busid_api.route('/v1/bus/<id>', methods=['GET'])
def busid_get(id):
    '''
    Get information about a single bus
    It is handler for GET /bus/<id>
    '''

    return jsonify()
