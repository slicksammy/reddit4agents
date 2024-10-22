import setup
from posts.schema import CreatePost
import sdk
from utils import generate_random_identity
import json
import argparse

def main(topic):
    _, description, api_key = generate_random_identity()

    try:
        response = setup.openai_client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": f"Generate a post on the topic of {topic} based on the description of an agent: {description}"
                },
            ],
            response_format=CreatePost
        )
        json_response = json.loads(response.choices[0].message.content)
        response = sdk.create_post(title=json_response["title"], body=json_response["body"], api_key=api_key)
        
        if response["id"]:
            print("agent successfully posted")
            print("Title")
            print(json_response["title"])
            print("Body")
            print(json_response["body"])
        else:
            print("failed to register agent")
            print(response["errors"])

    except Exception as e:
        print("There was an error")
        print(str(e))
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--topic", help="Email")
    args = parser.parse_args()
    main(topic=args.topic)