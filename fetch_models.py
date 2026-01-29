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
        num_models = len(models)
        half = (num_models + 1) // 2
        for i in range(half):
            # Left Column
            m1 = models[i]
            name1 = (m1[:42] + "...") if len(m1) > 45 else m1
            idx1 = i + 1
            col1 = f"[{idx1:2}] {name1}".ljust(52)
            
            # Right Column
            if i + half < num_models:
                m2 = models[i + half]
                name2 = (m2[:42] + "...") if len(m2) > 45 else m2
                idx2 = i + half + 1
                col2 = f"[{idx2:2}] {name2}"
                print(f"{col1} {col2}")
            else:
                print(col1)
        print(f"[ 0] Exit")
    else:
        print("No free models found or error occurred.")
