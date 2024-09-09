import sys
from pathlib import Path

# Add the parent directory to the system path
current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir))

from huggingface_hub import InferenceClient

from lib.config import load_config, get_hugging_face_api_key

load_config()


client = InferenceClient(
    "mattshumer/Reflection-Llama-3.1-70B",
    token=get_hugging_face_api_key(),
)


# Function to setup the llm response
def reflection_response(user_input):
    for message in client.chat_completion(
        messages=[{"role": "user", "content": user_input}],
        max_tokens=500,
        stream=True,
    ):
        return message.choices[0].delta.content