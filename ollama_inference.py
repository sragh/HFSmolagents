'''
This script demonstrates the usage of the Hugging Face Transformers library for text summarization using the SmolAgents framework.
It also incorporates tool calling and enables authorized imports for seamless operation.

Now modified to use Ollama instead of Hugging Face Inference API.
'''

import os
import subprocess
import requests
from bs4 import BeautifulSoup
from smolagents import CodeAgent, DuckDuckGoSearchTool

# Function to interact with Ollama

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

# Define a function to generate responses using Ollama

def generate_response(prompt, **kwargs):
    clean_prompt = str(prompt).strip()
    response_text = ollama_infer("qwen2.5-coder:latest", clean_prompt)  # Change model name as needed

    class Response:
        def __init__(self, text):
            self.content = text  # Simulate the expected response object format
    
    return Response(response_text)

# Define tools (DuckDuckGo for web search)
tools = [DuckDuckGoSearchTool()]

# Create the agent
agent = CodeAgent(tools=tools, model=generate_response, additional_authorized_imports=["requests", "bs4"])

# Example query to the agent:
query = "Summarize the main points of the Wikipedia article on Hugging Face (the company)."

# Run the agent with the query
result = agent.run(query)

print("Agent Output:", result)

# Directly fetch the Wikipedia page for Hugging Face
wikipedia_url = "https://en.wikipedia.org/wiki/Hugging_Face"

print("Fetching Wikipedia URL:", wikipedia_url)

try:
    # Fetch and parse the Wikipedia page
    response = requests.get(wikipedia_url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.content, 'html.parser')
    content_div = soup.find('div', {'class': 'mw-parser-output'})
    paragraphs = content_div.find_all('p') if content_div else []

    # Summarize the main points
    main_points = [p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)]
    
    for i, point in enumerate(main_points[:5], 1):  # Limit to first 5 points for brevity
        print(f"Main Point {i}: {point}")
    
    # Use the first few paragraphs as the summary
    summary = " ".join(main_points[:3])  # Adjust as needed
    print("\nSummary:\n", summary)

except requests.RequestException as e:
    print(f"Failed to fetch Wikipedia page: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
