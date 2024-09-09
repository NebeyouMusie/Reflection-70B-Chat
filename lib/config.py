import os
from dotenv import load_dotenv


# Function to load configuration for the environment varialbles
def load_config():
    return load_dotenv()

# Function to retrieve GROQ API KEY
def get_hugging_face_api_key():
    return os.getenv('HUGGING_FACE_TOKEN')