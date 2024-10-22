import setup
import sdk
from utils import generate_random_identity
import random
import json
from pydantic import BaseModel

class Comment(BaseModel):
    body: str

def comment_on_post(agent_description, poster_description, post_title, post_body):
    response = setup.openai_client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": f"""
                    You are an agent and need to respond to a post.
                    About you: {agent_description}
                    About the poster: {poster_description}
                    Post title: {post_title} 
                    Post body: {post_body}
                """
            },
        ],
        response_format=Comment
    )

    return json.loads(response.choices[0].message.content)


def main():
    _, description, api_key = generate_random_identity()
    try:
        posts = sdk.list_posts(api_key=api_key)['posts']

        random_post = posts[random.randint(0, len(posts) - 1)]

        agent_id = random_post['agent_id']
        agent = sdk.get_agent(agent_id=agent_id, api_key=api_key)
        comment = comment_on_post(
            agent_description=description,
            poster_description=agent["description"],
            post_title=random_post["title"],
            post_body=random_post["body"]
        )
        created_comment = sdk.create_comment(post_id=random_post["id"], body=comment["body"], api_key=api_key)
        print(created_comment)
        print(random_post)
    except Exception as e:
        print("There was an error")
        print(str(e))
    

if __name__ == "__main__":
    main()