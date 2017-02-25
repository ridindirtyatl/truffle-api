from flask import Blueprint, jsonify, request


bus_api = Blueprint('bus_api', __name__)


@bus_api.route('/v1/bus', methods=['GET'])
def bus_get():
    '''
    Get a list of all buses
    It is handler for GET /bus
    '''

    return jsonify()


@bus_api.route('/v1/bus/<id>', methods=['GET'])
def bus_byId_get(id):
    '''
    Get information about a single bus
    It is handler for GET /bus/<id>
    '''

    return jsonify()
