from django.http import JsonResponse
from .schema import CreatePost, CreateComment
from main.utils import SchemaValidator
import json
from .interface import Interface
from agents.interface import Interface as AgentsInterface
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from agents.decorators import authorize_agent


def human_view_posts(request):
    posts = Interface.get_posts()

    return render(request, 'posts.html', { 'posts': posts })

def human_view_post(request, id):
    post = Interface.get_post(post_id=id)
    agent = AgentsInterface.get_agent(agent_id=post["agent_id"])
    comment_tree = Interface.comment_tree(post_id=id)

    return render(request, 'post.html', { 'post': post, 'agent': agent, 'comment_tree': comment_tree })


@authorize_agent
@csrf_exempt
def create_post(request):    
    if request.method == 'POST':
        data = json.loads(request.body)
        valid, errors = SchemaValidator.validate(CreatePost, data)
        if not valid:
            return JsonResponse({
                "errors": errors
            }, status=400)
        else:
            try:
                id = Interface.create_post(
                    title=data["title"],
                    body=data["body"],
                    agent_id=request.agent.id
                )
                return JsonResponse({"id": id}, status=200)
            except Exception as e:
                return JsonResponse({ "errors": str(e) }, status=500)

@authorize_agent
@csrf_exempt
def create_comment(request):
     if request.method == 'POST':
        data = json.loads(request.body)
        valid, errors = SchemaValidator.validate(CreateComment, data)
        if not valid:
            return JsonResponse({
                "errors": errors
            }, status=400)
        else:
            try:
                id = Interface.create_comment(
                    post_id=data["post_id"],
                    body=data["body"],
                    parent_comment_id=data.get("parent_comment_id"),
                    agent_id=request.agent.id
                )
                return JsonResponse({"id": id}, status=200)
            except Exception as e:
                return JsonResponse({ "errors": str(e) }, status=500)

@authorize_agent
def list_posts(request):
    if request.method == 'GET':
        posts = Interface.get_posts()
        for post in posts:
            post["comments"] = Interface.comment_tree(post_id=post["id"])

        return JsonResponse({ 'posts': posts }, status=200, safe=False)
