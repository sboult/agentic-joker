# Bedrock Joke Agent

A simple agent that uses Strands Agents SDK with Amazon Bedrock to tell you a joke about Python.

## Setup

```bash
# Create a virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate

# Install dependencies
pip install strands-agents

# Run the agent
python main.py
```

## Prerequisites

- AWS credentials configured (`aws configure` or environment variables)
- Bedrock model access enabled in your AWS account (Claude 4 in us-east-1)
