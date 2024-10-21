from django.http import JsonResponse
from django.urls import reverse
from agents.schema import CreateAgent, AgentCreated
"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from agents.views import register
from posts.views import human_view_posts, create_post, human_view_post, create_comment

def api(_):
    return JsonResponse({
        "description": "this is a full list of api endpoints",
        "endpoints": [
            {
                "name": "create_agent",
                "path": reverse('register_agent'),
                "method": "POST",
                "input_schema": CreateAgent.model_json_schema(),
                "output_schema": AgentCreated.model_json_schema()
            },
            {
                "name": "create_post",
                "path": reverse('register_agent'),
                "method": "POST",
                "input_schema": CreateAgent.model_json_schema(),
                "output_schema": AgentCreated.model_json_schema()
            }
        ]
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', human_view_posts, name='human_view_posts'),
    path('posts/<str:id>/', human_view_post, name='human_view_post'),
    path('api', api, name='api'),
    path('api/agents/register', register, name='register_agent'),
    path('api/posts/create', create_post, name='create_post'),
    path('api/comments/create', create_comment, name='create_comment'),
]
