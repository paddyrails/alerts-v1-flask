from flask import Blueprint, request, jsonify
from service.alert_service import AlertDefinitionService
from common.schemas import alert_definition_schema, alert_definitions_schema

alert_definitions_bp = Blueprint('alert_definitions', __name__, url_prefix='/api/v1/alert-definitions')

service = AlertDefinitionService()

# Get all alert definitions
@alert_definitions_bp.route('/', methods=['GET'])
def get_all():
    alert_definitions = service.get_all()
    return alert_definitions_schema.jsonify(alert_definitions), 200

#Get alert by id
@alert_definitions_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    try:
        alert_definition = service.get_by_id(id)
        return alert_definition_schema.jsonify(alert_definition), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    
#Create AlertDefition
@alert_definitions_bp.route('/', methods=['POST'])
def create():
    try:
        data = request.get_json(force=True)
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        alert_definition = service.create(data)
        return alert_definition_schema.jsonify(alert_definition), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
#update AlertDefinition
@alert_definitions_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        alert_definition = service.update(id, data)
        return alert_definition_schema.jsonify(alert_definition)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    

# Delete alert definition
@alert_definitions_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    try: 
        service.delete(id)
        return jsonify({'message': "Alert Definition deleted successfully"}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    