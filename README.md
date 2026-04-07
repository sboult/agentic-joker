# Bedrock Joke Agent

> **⚠️ This is a sample repository for demonstration purposes only.** It is not intended for production use.

A simple agent built with [Strands Agents SDK](https://github.com/strands-agents/sdk-python) and [Amazon Bedrock](https://aws.amazon.com/bedrock/) that tells you a joke about Python.

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
