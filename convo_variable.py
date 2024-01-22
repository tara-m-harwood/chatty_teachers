#!/home/tarastar42/.virtualenvs/myvirtualenv/bin/python

import requests
import json
import os
from dotenv import load_dotenv

# Set our API key in a secure way
dotenv_path = '/home/tarastar42/.env'
load_dotenv(dotenv_path)
api_key = os.environ.get("OPENAI_API_KEY")

# Define the starting point of a conversation

convo = [{'role': 'system', 'content': "You are a helpful assistant."}]

def api_call(messages):
    # Define the headers for the api call
    headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
    }

    # Put together the payload for the API call
    data = {
    'model': 'gpt-4',  # Replace with your chosen model
    'messages': convo
    }

    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, data=json.dumps(data))
    print(response.json())

api_call(convo)
