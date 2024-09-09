import os
from dotenv import load_dotenv


# Function to load configuration for the environment varialbles
def load_config():
    return load_dotenv()

def get_openrouter_api_key():
    return os.getenv('OPENROUTER_API_KEY')