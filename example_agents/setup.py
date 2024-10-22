import sys
from dotenv import load_dotenv
import os
from openai import OpenAI

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
script_dir = os.path.dirname(os.path.realpath(__file__))
env_path = os.path.join(script_dir, '.env')
load_dotenv(dotenv_path=env_path)

script_dir = os.path.dirname(os.path.realpath(__file__))
creds_file_path = os.path.join(script_dir, f'agent_creds_{os.getenv('REDDIT_AGENT_ENV')}.csv')

if not os.path.exists(creds_file_path):
    with open(creds_file_path, 'w') as file:
        file.write('')  # Create an empty CSV file
    print(f"'{creds_file_path}' created.")

openai_client = OpenAI(
    api_key=os.getenv('OPEN_AI_API_KEY')
)