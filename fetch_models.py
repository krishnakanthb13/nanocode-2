import urllib.request
import json
import os

def fetch_free_models():
    """Fetches free models from OpenRouter API."""
    url = "https://openrouter.ai/api/v1/models"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            # Filter for models where prompt and completion prices are 0
            free_models = [
                m['id'] for m in data.get('data', [])
                if float(m.get('pricing', {}).get('prompt', 0)) == 0 and 
                   float(m.get('pricing', {}).get('completion', 0)) == 0
            ]
            return sorted(free_models)
    except Exception as e:
        print(f"Error fetching models: {e}")
        return []

if __name__ == "__main__":
    models = fetch_free_models()
    if models:
        print("Free OpenRouter Models:")
        for idx, model in enumerate(models, 1):
            print(f"{idx}. {model}")
    else:
        print("No free models found or error occurred.")
