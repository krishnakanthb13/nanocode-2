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
                m for m in data.get('data', [])
                if float(m.get('pricing', {}).get('prompt', 0)) == 0 and 
                   float(m.get('pricing', {}).get('completion', 0)) == 0
            ]
            return sorted(free_models, key=lambda x: x['id'])
    except Exception as e:
        print(f"Error fetching models: {e}")
        return []

def filter_models(models, filter_type):
    """Filters models based on capabilities."""
    if filter_type == "tools":
        return [m for m in models if "tools" in m.get("supported_parameters", [])]
    elif filter_type == "structured":
        return [m for m in models if "structured_outputs" in m.get("supported_parameters", [])]
    elif filter_type == "reasoning":
        return [m for m in models if "reasoning" in m.get("supported_parameters", []) or "include_reasoning" in m.get("supported_parameters", [])]
    elif filter_type == "vision":
        return [m for m in models if "image" in m.get("architecture", {}).get("modality", "")]
    return models

if __name__ == "__main__":
    all_free_models = fetch_free_models()
    if not all_free_models:
        print("No free models found or error occurred.")
        exit()

    filtered_models = all_free_models
    filter_choice = "all"

    while True:
        print(f"\nFree OpenRouter Models (Filter: {filter_choice}):")
        num_models = len(filtered_models)
        if num_models == 0:
            print("  No models match this filter.")
        else:
            half = (num_models + 1) // 2
            for i in range(half):
                m1 = filtered_models[i]['id']
                name1 = (m1[:42] + "...") if len(m1) > 45 else m1
                idx1 = i + 1
                col1 = f"[{idx1:2}] {name1}".ljust(52)
                
                if i + half < num_models:
                    m2 = filtered_models[i + half]['id']
                    name2 = (m2[:42] + "...") if len(m2) > 45 else m2
                    idx2 = i + half + 1
                    col2 = f"[{idx2:2}] {name2}"
                    print(f"{col1} {col2}")
                else:
                    print(col1)

        print("\nFilters:")
        print("  [ t] Tool Calling models")
        print("  [ s] Structured Output (JSON) models")
        print("  [ r] Reasoning (Thinking) models")
        print("  [ v] Vision (Image) models")
        print("  [ a] All free models")
        print("  [ 0] Exit")

        choice = input("\nSelect a filter or model index: ").strip().lower()
        
        if choice == '0':
            break
        elif choice == 't':
            filtered_models = filter_models(all_free_models, "tools")
            filter_choice = "Tool Calling"
        elif choice == 's':
            filtered_models = filter_models(all_free_models, "structured")
            filter_choice = "Structured Output"
        elif choice == 'r':
            filtered_models = filter_models(all_free_models, "reasoning")
            filter_choice = "Reasoning"
        elif choice == 'v':
            filtered_models = filter_models(all_free_models, "vision")
            filter_choice = "Vision"
        elif choice == 'a':
            filtered_models = all_free_models
            filter_choice = "all"
        else:
            try:
                idx = int(choice)
                if 1 <= idx <= len(filtered_models):
                    print(f"Selected: {filtered_models[idx-1]['id']}")
                    break
                else:
                    print("Invalid index.")
            except ValueError:
                print("Invalid input.")
