import os
import subprocess
import sys
from pathlib import Path

# Add project root to sys.path so we can import fetch_models
project_root = Path(__file__).parent.absolute()
sys.path.append(str(project_root))

from fetch_models import fetch_free_models, filter_models

def load_env():
    env_path = project_root / ".env"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                if "=" in line and not line.startswith("#"):
                    k, v = line.strip().split("=", 1)
                    os.environ.setdefault(k, v)

def select_model():
    load_env()
    
    print("Fetching free models from OpenRouter...")
    all_free_models = fetch_free_models()
    
    if not all_free_models:
        print("Could not fetch models. Defaulting to anthropic/claude-3.5-sonnet")
        return "anthropic/claude-3.5-sonnet"

    filtered_models = all_free_models
    filter_choice = "all"

    while True:
        print(f"\nAvailable Free Models (Filter: {filter_choice}):")
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
        
        choice = input(f"\nSelect a filter or model [0-{num_models}] (default 1): ").strip().lower()
        if not choice:
            return filtered_models[0]['id']
        
        if choice == '0':
            print("Exiting...")
            sys.exit(0)
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
                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(filtered_models):
                    return filtered_models[choice_idx]['id']
                else:
                    print(f"Please enter a number between 0 and {len(filtered_models)}.")
            except ValueError:
                print("Invalid input. Please enter a number or filter key.")

def main():
    model = select_model()
    os.environ["MODEL"] = model
    
    # Enable reasoning/thinking if using OpenRouter
    if "/" in model: 
        os.environ["INCLUDE_REASONING"] = "true"
    
    print(f"\nStarting nanocode with model: {model}\n")
    
    # Run nanocode.py using its absolute path
    try:
        nanocode_path = project_root / "nanocode.py"
        subprocess.run([sys.executable, str(nanocode_path)], check=True)
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"Error running nanocode: {e}")

if __name__ == "__main__":
    main()
