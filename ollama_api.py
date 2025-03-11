#use this code to create an API that can be used to interact with Ollama.
'''
This script is used to create a FastAPI-based API for interacting with Ollama models.
This ollama is on your local machine and you can use it to interact with the models.

For MacBook only:
Check your version of ollama by running `ollama --version` in the terminal.
If you don't have ollama installed, you can install it using Homebrew:
`brew install ollama`
To get a list of available models, run `ollama list`.
To pull a model, run `ollama pull <model_name>`.
To run inference, use `ollama run <model_name> <prompt>`.
'''
from fastapi import FastAPI
import subprocess

app = FastAPI()

def ollama_infer(model, prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", model, prompt],
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {e}"

@app.get("/infer")
def infer(model: str, prompt: str):
    response = ollama_infer(model, prompt)
    return {"model": model, "response": response}

# Run the API with:
# uvicorn ollama_api:app --host 0.0.0.0 --port 8000
