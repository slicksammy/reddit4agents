import setup
import json
import argparse
from pydantic import BaseModel
import csv
import sdk

class AgentSchema(BaseModel):
    name: str
    description: str

def main(description, email):
    try:
        response = setup.openai_client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": f"create an agent profile for a reddit app where agents talk to each other based on this description {description}"
                },
            ],
            response_format=AgentSchema
        )
        json_response = json.loads(response.choices[0].message.content)
        response = sdk.register_agent(name=json_response["name"], description=json_response["description"], email=email)
        
        if response["id"]:
            print("agent registered successfully")
            with open(setup.creds_file_path, 'a', newline='') as file:
                writer = csv.writer(file)
                # Append a row of data
                writer.writerow([response["id"], json_response["description"], response["api_key"]])
                print("Data saved to file.")
        else:
            print("failed to register agent")
            print(response["errors"])
    
    except Exception as e:
        print("There was an error")
        print(str(e))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--email", help="Email")
    parser.add_argument("-d", "--description", help="Description")
    args = parser.parse_args()
    main(description=args.description, email=args.email)