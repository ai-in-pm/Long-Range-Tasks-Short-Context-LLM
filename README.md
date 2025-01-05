# PRISM AI Agent

This project implements an AI agent based on the PRISM (Processing Incrementally with Structured Memory) approach. The system demonstrates how to process long-range reasoning tasks using a short-context LLM by maintaining a structured memory representation and leveraging OpenAI's GPT models for advanced text processing.

The development of this GitHub Repository was inspired by the "Long-Range Tasks Using Short-Context LLMs:
Incremental Reasoning With Structured Memories" Paper. To read the entire paper, visit https://arxiv.org/pdf/2412.18914 

## Features

- **Incremental Processing**: Process large inputs in manageable chunks
- **Structured Memory**: Hierarchical memory representation with efficient key-value caching
- **Memory Management**: Automatic memory capacity management to prevent overflow
- **Performance Metrics**: Track processing time, memory usage, and chunk sizes
- **Type Safety**: Full type hints for better code maintainability
- **OpenAI Integration**: Utilizes GPT models for intelligent text summarization

## Project Structure

- **src/**: Main source code for the AI agent
  - `prism_agent.py`: Core PRISM implementation
- **tests/**: Unit tests for the implemented functionality
  - `test_prism.py`: Comprehensive test suite
- **schemas/**: JSON schema definitions for structured memory
- **docs/**: Additional documentation

## Prerequisites

1. Create a `.env` file in the root directory with your OpenAI API key:
```
OPENAI_API_KEY="your-api-key-here"
```

2. Python 3.8 or higher is required.

## Setup

### 1. Create and Activate Virtual Environment

#### Windows
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
.\.venv\Scripts\activate
```

#### macOS/Linux
```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

### 2. Install Dependencies

With the virtual environment activated, install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

```python
from src.prism_agent import PRISM

# Initialize PRISM with a memory capacity and specific model
prism = PRISM(memory_capacity=1000, model="gpt-4")

# Process text chunks
chunks = [
    {'text': 'Your text chunk here...'},
    # Add more chunks as needed
]

# Process the chunks
prism.process_chunks(chunks)

# Get performance metrics
metrics = prism.get_performance_metrics()
print(metrics)
```

## Performance Metrics

The system tracks several performance metrics:
- Average processing time per chunk
- Maximum memory usage
- Average chunk size
- Token usage for API calls

## Environment Variables

The following environment variables are required:
- `OPENAI_API_KEY`: Your OpenAI API key

## Testing

With the virtual environment activated, run the test suite:

```bash
python -m unittest tests/test_prism.py
```

## Security Note

Never commit your `.env` file or expose your API key. The `.env` file is included in `.gitignore` by default.

## Deactivating Virtual Environment

When you're done working on the project, deactivate the virtual environment:

```bash
deactivate
