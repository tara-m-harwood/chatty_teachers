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

def get_response(messages):
    # Define the headers for the api call
    headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
    }

    # Put together the payload for the API call
    data = {
    'model': 'gpt-3.5-turbo',
    'messages': messages
    }

    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, data=json.dumps(data))
    response = response.json()
    #print(response)

    message_content = response['choices'][0]['message']['content']
    print(message_content)

def ask_user(messages):
    user_input = input()
    new_message = {'role': 'user', 'content': user_input}
    messages.append(new_message)
    return messages

while True:
    get_response(convo)
    convo = ask_user(convo)

