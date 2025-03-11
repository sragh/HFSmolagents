# CLAUDE.md - Project Guidelines

## Run Commands
- Run main application: `python app.py`
- Run Ollama inference: `python ollama_inference.py`
- Run Msty inference: `python msty_inference.py`
- Run Ollama API server: `uvicorn ollama_api:app --host 0.0.0.0 --port 8000`
- Ollama CLI: `ollama run <model_name> "<prompt>"`
- List Ollama models: `ollama list`

## Code Style Guidelines
- **Imports**: Group standard library imports first, third-party imports second, local imports last
- **Docstrings**: Use triple single quotes (`'''`) for module/script-level docstrings
- **Error Handling**: Use try/except blocks with specific exceptions, log error details
- **Naming**: Use snake_case for functions/variables, CamelCase for classes
- **Type Hints**: Not currently used but encouraged for new code
- **Line Length**: ~80-100 characters preferred
- **Formatting**: Use 4 spaces for indentation
- **Function Structure**: Small, focused functions with clear input/output

## Project Structure
- Uses smolagents framework for agent functionality
- Supports multiple inference backends (HuggingFace, Ollama, Msty)
- Implements web search capabilities via DuckDuckGoSearchTool