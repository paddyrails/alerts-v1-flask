from dao.alert_dao import AlertDefinitionDAO
from common.models.alert_definition import AlertDefinition

dao = AlertDefinitionDAO()

class AlertDefinitionService:

    def get_all(self):
        return dao.get_all()
    
    def get_by_id(self, id):
        alert_definition = dao.get_by_id(id)
        if not alert_definition:
            raise ValueError(f'Alert definition with id {id} not found')
        return alert_definition
    
    def create(self, data):
        print("Received data:", data)
        self._validate(data)
        alert_definition = AlertDefinition(
            title=data['title'],
            description=data['description'],
            configuration=data['configuration']
        )
        return dao.create(alert_definition)
    
    def update(self, id, data):
        alert_definition = self.get_by_id(id)
        if 'title' in data:
            self._validate_title(data['title'])
        alert_definition.title = data.get('title', alert_definition.title)
        alert_definition.description = data.get('description', alert_definition.description)
        alert_definition.configuration = data.get('configuration', alert_definition.configuration)
        alert_definition.is_active =  data.get('is_active', alert_definition.is_active)
        return dao.update(alert_definition)
    
    def delete(self, id):
        alert_definition = self.get_by_id(id)
        dao.delete(alert_definition)

    def _validate(self, data):
        if not data.get('title'):
            raise ValueError('Title is required')
        if not data.get('description'):
            raise ValueError('Decription is required')
        if not data.get('configuration'):
            raise ValueError('Configuration is required')
        if not isinstance(data.get('configuration'), dict):
            raise ValueError("Configuration must be JSON object")
        self._validate_title(data['title'])

    def _validate_title(self, title):
        if len(title) > 100:
            raise ValueError('Title must be 100 characters or less')

