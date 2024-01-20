#!/home/tarastar42/.virtualenvs/myvirtualenv/bin/python

import requests
import json
import os
from dotenv import load_dotenv
#from openai import OpenAI

# Set your OpenAI API key

dotenv_path = '/home/tarastar42/.env'
load_dotenv(dotenv_path)
api_key = os.environ.get("OPENAI_API_KEY")

# Define the headers
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
}

# Chat Completions request data
data = {
    'model': 'gpt-4',  # Replace with your chosen model
    'messages': [
        {'role': 'system', 'content': "You are a helpful assistant."},
        {'role': 'user', 'content': "Hey pal!  What's the word?"}
    ]
}

response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, data=json.dumps(data))
print(response.json())
