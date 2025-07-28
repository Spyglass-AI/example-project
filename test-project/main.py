import os
import time
import yaml
import openai
from dotenv import load_dotenv
from spyglass_ai import spyglass_openai, spyglass_trace

# Load environment variables from .env file
load_dotenv()

def load_model_config():
    """Load model configuration from model.yaml file."""
    try:
        with open("model.yaml", "r") as file:
            config = yaml.safe_load(file)
            return config.get("model"), config.get("prompt")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

@spyglass_trace()
def call_openai_chat_api(model, system_prompt):
    try:
        print("Attempting to call OpenAI Chat API...")
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": "Tell me a joke with only two sentences."}
            ]
        )
        if completion.choices:
            print("OpenAI Response:", completion.choices[0].message.content)
        else:
            print("OpenAI Response: No choices returned")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Check for required environment variables
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable not set.")
        print("Please copy .env.example to .env and set your API keys.")
    elif not os.getenv("SPYGLASS_API_KEY"):
        print("Error: SPYGLASS_API_KEY environment variable not set.")
        print("Please copy .env.example to .env and set your API keys.")
    elif not os.getenv("SPYGLASS_DEPLOYMENT_ID"):
        print("Error: SPYGLASS_DEPLOYMENT_ID environment variable not set.")
        print("Please copy .env.example to .env and set your deployment ID.")
    else:
        # Load configuration from model.yaml
        model, system_prompt = load_model_config()
        
        openai.api_key = os.getenv("OPENAI_API_KEY")
        # Wrap OpenAI client
        client = spyglass_openai(openai.OpenAI())

        print("Starting OpenAI API call loop (every 3 seconds)...")
        try:
            while True:
                call_openai_chat_api(model, system_prompt)
                print("Waiting 3 seconds before next call...")
                time.sleep(3)
        except KeyboardInterrupt:
            print("\nStopping the loop. Goodbye!") 