import json
import requests
from lib.config import get_openrouter_api_key

OPENROUTER_API_KEY = get_openrouter_api_key()

def reflection_response(user_input):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}"
        },
        data=json.dumps({
            "model": "mattshumer/reflection-70b:free",
            "messages": [
                { "role": "user", "content": user_input }
            ]
        })
    )
    
    # Parse the JSON response
    data = response.json()
    
    # Return the content of the AI response
    return data['choices'][0]['message']['content']