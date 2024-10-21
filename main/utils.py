from pydantic import ValidationError

class SchemaValidator:
    @classmethod
    def validate(cls, schema, data):
        try:
            schema(**data)
        except ValidationError as e:
            return [False, e.errors()]
        
        return [True, None]