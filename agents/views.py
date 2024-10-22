from django.shortcuts import render
from django.http import JsonResponse
from .schema import CreateAgent
from main.utils import SchemaValidator
import json
from .interface import Interface
from django.views.decorators.csrf import csrf_exempt
from .decorators import authorize_agent

@csrf_exempt
def register(request):    
    if request.method == 'POST':
        data = json.loads(request.body)
        valid, errors = SchemaValidator.validate(CreateAgent, data)
        if not valid:
            return JsonResponse({
                "errors": errors
            }, status=400)
        else:
            try:
                id, api_key = Interface.create_agent(
                    name=data["name"],
                    description=data["description"],
                    email=data["email"]
                )
                return JsonResponse({"id": id, "api_key": api_key}, status=200)
            except Exception as e:
                return JsonResponse({ "errors": str(e)}, status=500)

@authorize_agent
def get_agent(request):
    if request.method == 'GET':
        try:
            agent_id = request.GET['id']
            agent = Interface.get_agent(agent_id=agent_id)
            return JsonResponse(agent, status=200)
        except Exception as e:
            return JsonResponse({ "errors": str(e)}, status=500)
