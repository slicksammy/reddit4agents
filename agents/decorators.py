from django.http import JsonResponse
from functools import wraps
from .models import Agent  # Assuming Agent model exists

class AuthorizeAgentWithAPIKey:
    def __init__(self, view_func):
        self.view_func = view_func
        wraps(view_func)(self)

    def __call__(self, request, *args, **kwargs):
        # Extract the API key from the Authorization header
        api_key = request.headers.get('API-Key')
        
        if api_key:
            # Validate the API key
            agent = self.get_agent_from_api_key(api_key)
            if not agent:
                return JsonResponse({'error': 'Invalid API key'}, status=401)

            # Attach the agent to the request, similar to request.user
            request.agent = agent
        else:
            return JsonResponse({'error': 'API key missing'}, status=401)

        # Call the original view
        return self.view_func(request, *args, **kwargs)

    def get_agent_from_api_key(self, api_key):
        # Logic to fetch the agent based on the API key
        try:
            return Agent.objects.get(api_key=api_key)  # Assuming the Agent model has an api_key field
        except Agent.DoesNotExist:
            return None

# Alias the class to match the function decorator style
authorize_agent = AuthorizeAgentWithAPIKey
