# Inference Playground

Welcome to the **Inference Playground**! This repository showcases a versatile setup for text summarization and interactive AI-powered inference using multiple backends. It leverages the Hugging Face Transformers library, the SmolAgents framework, and integrates tools like Ollama and Msty to deliver engaging, multi-faceted AI interactions.

---

## Features

- **Multi-Backend Inference:**  
  Choose between Hugging Face, Ollama, or Msty to generate responses, giving you flexibility in your deployment.

- **Agent-Based Interaction:**  
  Harness the power of the SmolAgents framework to combine dynamic inference with tool calling (e.g., web search via DuckDuckGo) for complex query processing.

- **Text Summarization:**  
  Automatically summarize key points from the Wikipedia article on Hugging Face using either agent-based processing or direct web scraping.

- **FastAPI Integration:**  
  Build your own API with our FastAPI-based server to interact with local Ollama models—perfect for rapid prototyping and local deployments.

- **Extensible & Customizable:**  
  Easily add your own tools and authorize additional imports to extend the agent's functionality without waiting for manual approvals.

---

## Getting Started

### Prerequisites

- **Python 3.8+**
- **Ollama:** Install via Homebrew on MacOS (`brew install ollama`)
- **Hugging Face Hub API Token:** [Get your token here](https://huggingface.co/settings/tokens)
- **Msty:** (If using the Msty inference module)
- **FastAPI & Uvicorn:** For running the API server

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/inference-playground.git
   cd inference-playground
   ```

2. **Install Dependencies:**
   Ensure your `requirements.txt` includes all needed packages (e.g., `smolagents`, `huggingface_hub`, `requests`, `beautifulsoup4`, `fastapi`).
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Token:**
   Replace `"your_huggingface_api_token_here"` in the code with your actual Hugging Face API token or set it as an environment variable.

---

## Usage

This repository contains several scripts to demonstrate different inference methods and agent functionalities:

### Hugging Face Inference with SmolAgents (Text Summarization)
- **Description:** Uses the Hugging Face Inference API with SmolAgents to summarize the main points from the Wikipedia page on Hugging Face.
- **Run:**
  ```bash
  python app.py
  ```

### Msty Inference (Interactive)
- **Description:** Lists available Msty models and runs inference based on user input.
- **Run:**
  ```bash
  python msty_inference.py
  ```

### Ollama Inference with SmolAgents
- **Description:** Demonstrates how to integrate local Ollama inference within the SmolAgents framework.
- **Run:**
  ```bash
  python ollama_inference.py
  ```

### Ollama API Server (FastAPI)
- **Description:** Provides a FastAPI-based endpoint to interact with local Ollama models.
- **Run:**
  ```bash
  uvicorn ollama_api:app --host 0.0.0.0 --port 8000
  ```

### Project Guidelines
- **Description:** Refer to `CLAUDE.md` for run commands, code style guidelines, and project structure details.

---

## Project Structure

```
inference-playground/
│
├── app.py         # Text summarization using Hugging Face Inference and SmolAgents.
├── msty_inference.py         # Interactive Msty inference example.
├── ollama_inference.py         # Ollama inference using SmolAgents.
├── ollama_api.py         # FastAPI-based API for local Ollama inference.
├── CLAUDE.md        # Project guidelines and run commands.
└── README.md        # This file.
```

---

## Contributing

Contributions are welcome! If you have ideas or improvements, please open an issue or submit a pull request. Make sure to follow the guidelines in `CLAUDE.md` for code style and structure.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- **SmolAgents Framework:** For enabling a flexible agent-based approach.
- **Hugging Face:** For providing an amazing ecosystem around AI and Transformers.
- **Ollama:** For the local inference capability.
- **DuckDuckGo Search:** For robust web search integration.

---

Dive in, experiment, and have fun exploring the world of multi-backend AI inference. Happy coding!
