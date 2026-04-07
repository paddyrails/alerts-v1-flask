from common.extensions import ma
from common.models.alert_definition import AlertDefinition

class AlertDefinitionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AlertDefinition
        load_instance = True
        include_fk = True

alert_definition_schema = AlertDefinitionSchema()
alert_definitions_schema = AlertDefinitionSchema(many=True)