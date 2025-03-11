'''
This script is used to demonstrate usage of HuggingFace Transformers library for 
text summarization using smolagents framework. It also demonstrates usage of tool 
calling and enabling authorized imports to facilitate the demonstration of seemless
working of the set-up.

You can add your own tools and imports for the framework to authorize instead of
waiting for your approval. Be careful with this though.
'''
import os
from smolagents import CodeAgent, DuckDuckGoSearchTool
from huggingface_hub import InferenceClient
import requests
from bs4 import BeautifulSoup

# Store the Hugging Face API token in environment variables
HUGGINGFACEHUB_API_TOKEN = "your_huggingface_api_token_here"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN

# Initialize the Inference Client
inference = InferenceClient(
    model="Qwen/Qwen2.5-Coder-32B-Instruct",
    token=HUGGINGFACEHUB_API_TOKEN
)

# Define a function to generate responses using the Inference Client
def generate_response(prompt, **kwargs):
    # Ensure prompt is a clean plain string
    clean_prompt = str(prompt).strip()
    
    # Use `.chat_completion()` directly with a clean prompt
    raw_response = inference.chat_completion(
        model="Qwen/Qwen2.5-Coder-32B-Instruct",
        messages=[{"role": "user", "content": clean_prompt}],
        max_tokens=500  # Limit response length
    )
    
    # Print raw response for debugging (optional)
    print("Raw Response:", raw_response)
    
    # Check if the response is a dictionary and extract text
    if isinstance(raw_response, dict) and "choices" in raw_response:
        generated_text = raw_response["choices"][0]["message"]["content"]
    else:
        generated_text = str(raw_response)
    
    # Wrap the text in an object with a `content` attribute for compatibility with CodeAgent
    class Response:
        def __init__(self, text):
            self.content = text  # Simulate the expected response object format
    
    return Response(generated_text)

# Define tools (DuckDuckGo for web search)
tools = [DuckDuckGoSearchTool()]

# Create the agent
agent = CodeAgent(tools=tools, model=generate_response, additional_authorized_imports=["requests", "bs4"])

# Example query to the agent:
query = "Summarize the main points of the Wikipedia article on Hugging Face (the company)."

# Run the agent with the query
result = agent.run(query)

# Directly fetch the Wikipedia page for Hugging Face
wikipedia_url = "https://en.wikipedia.org/wiki/Hugging_Face"

print("Fetching Wikipedia URL:", wikipedia_url)

try:
    # Fetch and parse the Wikipedia page
    response = requests.get(wikipedia_url)
    response.raise_for_status()  # Raise an error for HTTP issues

    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the main content of the page
    content_div = soup.find('div', {'class': 'mw-parser-output'})
    paragraphs = content_div.find_all('p') if content_div else []

    # Summarize the main points
    main_points = []
    for p in paragraphs:
        text = p.get_text(strip=True)
        if text:
            main_points.append(text)

    # Print the main points
    for i, point in enumerate(main_points[:5], 1):  # Limit to first 5 points for brevity
        print(f"Main Point {i}: {point}")

    # Use the first few paragraphs as the summary
    summary = " ".join(main_points[:3])  # Adjust this if more/less is needed
    print("\nSummary:\n", summary)

except requests.RequestException as e:
    print(f"Failed to fetch Wikipedia page: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
