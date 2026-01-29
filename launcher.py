import os
import subprocess
import sys
from pathlib import Path

# Add project root to sys.path so we can import fetch_models
project_root = Path(__file__).parent.absolute()
sys.path.append(str(project_root))

from fetch_models import fetch_free_models

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
    models = fetch_free_models()
    
    if not models:
        print("Could not fetch models. Defaulting to anthropic/claude-3.5-sonnet")
        return "anthropic/claude-3.5-sonnet"

    print("\nAvailable Free Models:")
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
    
    while True:
        try:
            choice = input(f"\nSelect a model [0-{len(models)}] (default 1): ").strip()
            if not choice:
                return models[0]
            choice_idx = int(choice) - 1
            if choice == "0":
                print("Exiting...")
                sys.exit(0)
            if 0 <= choice_idx < len(models):
                return models[choice_idx]
            else:
                print(f"Please enter a number between 0 and {len(models)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    model = select_model()
    os.environ["MODEL"] = model
    
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
