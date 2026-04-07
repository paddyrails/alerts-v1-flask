from common.extensions import db
from common.models.alert_definition import AlertDefinition

class AlertDefinitionDAO:
    def get_all(self):
        return AlertDefinition.query.all()
    
    def get_by_id(self, id):
        return AlertDefinition.query.get(id)
    
    def create(self, alert_definition):
        db.session.add(alert_definition)
        db.session.commit()
        return alert_definition
    
    def update(self, alert_definition):
        db.session.commit()
        return alert_definition
    
    def delete(self, alert_definition):
        db.session.delete(alert_definition)
        db.session.commit()