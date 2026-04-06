import boto3
import json

client = boto3.client("bedrock-runtime", region_name="us-east-1")

response = client.converse(
    modelId="us.anthropic.claude-opus-4-6-v1",
    messages=[
        {
            "role": "user",
            "content": [
                {"text": "Tell me a joke about Python (the programming language)."}
            ],
        }
    ],
    inferenceConfig={"maxTokens": 256},
)

print(response["output"]["message"]["content"][0]["text"])
