import subprocess

# Function to list available models on Msty
def list_msty_models():
    print("Listing available Msty models...")
    result = subprocess.run("msty models", shell=True, capture_output=True, text=True)
    models = result.stdout.strip().split("\n")
    print("\nAvailable Models:")
    for i, model in enumerate(models, 1):
        print(f"{i}. {model}")
    return models

# Function to run inference on Msty
def run_msty_inference(model_name, prompt):
    print(f"\nRunning inference using model: {model_name}...")
    command = f'msty run {model_name} --input "{prompt}"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print("Error occurred during inference:")
        print(result.stderr)
        return None
    else:
        response = result.stdout.strip()
        return response

# Main function to handle user input and model selection
def main():
    # List available models
    models = list_msty_models()
    
    # Get model choice from user
    while True:
        try:
            choice = int(input("\nEnter the model number to use (e.g., 1 for the first model): "))
            if 1 <= choice <= len(models):
                selected_model = models[choice - 1]
                break
            else:
                print(f"Please enter a number between 1 and {len(models)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Get user query
    query = input("\nEnter your query (e.g., 'Summarize the main points of the Wikipedia article on Hugging Face'): ")
    
    # Run inference
    response = run_msty_inference(selected_model, query)
    
    # Print the result
    if response:
        print("\nGenerated Response:")
        print(response)
    else:
        print("No response generated.")

if __name__ == "__main__":
    main()
