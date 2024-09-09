import sys
from pathlib import Path

# Add the parent directory to the system path
current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir))


from lib.config import load_config, get_hugging_face_api_key

load_config()

# Function to setup the llm
def reflection_response():
    llm = ChatGroq(
        model='gemma2-9b-it',
        temperature=0.7,
        api_key=get_groq_api_key()
    )
    return llm