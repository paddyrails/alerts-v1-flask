from flask import Blueprint
from api.alert_controller import alert_definitions_bp

def register_blueprints(app):
    app.register_blueprint(alert_definitions_bp)