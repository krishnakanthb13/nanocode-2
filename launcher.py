import os
import subprocess
import sys
from fetch_models import fetch_free_models

def load_env():
    if os.path.exists(".env"):
        with open(".env") as f:
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
    for idx, model in enumerate(models, 1):
        print(f"[{idx}] {model}")
    
    while True:
        try:
            choice = input(f"\nSelect a model [1-{len(models)}] (default 1): ").strip()
            if not choice:
                return models[0]
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(models):
                return models[choice_idx]
            else:
                print(f"Please enter a number between 1 and {len(models)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    model = select_model()
    os.environ["MODEL"] = model
    
    print(f"\nStarting nanocode with model: {model}\n")
    
    # Run nanocode.py
    try:
        subprocess.run([sys.executable, "nanocode.py"], check=True)
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"Error running nanocode: {e}")

if __name__ == "__main__":
    main()
