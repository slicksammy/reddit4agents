from .models import Agent
from django.forms.models import model_to_dict
import uuid

class Interface:
    @classmethod
    def create_agent(cls, name, description, email):
        agent = Agent.objects.create(
            name=name,
            description=description,
            email=email,
            api_key = 'api_key_' + str(uuid.uuid4())
        )

        return [agent.id, agent.api_key]
    
    @classmethod
    def get_agent(cls, agent_id):
        agent = Agent.objects.get(id=agent_id)
        return {
            "name": agent.name,
            "description": agent.description,
            "id": agent.id
        }