# Bedrock Joke Agent

A simple script that uses Amazon Bedrock to tell you a joke about Python.

## Setup

```bash
# Create a virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate

# Install dependencies
pip install boto3

# Run the script
python main.py
```

## Prerequisites

- AWS credentials configured (`aws configure` or environment variables)
- Bedrock model access enabled in your AWS account (us-east-1)
