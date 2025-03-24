import openai
import json
import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

# # Azure OpenAI Configuration
# AZURE_OPENAI_ENDPOINT = "https://ai-service-for-sachin.openai.azure.com/"
# AZURE_OPENAI_API_KEY = "ui4yDQxobmZOtfgZ2NVz4DTMB7qyUT7gSOwzlc6CpavLcQyKc7eWJQQJ99BCACfhMk5XJ3w3AAAAACOGvv7S"
# AZURE_OPENAI_API_VERSION = "2024-02-15-preview"
# AZURE_OPENAI_DEPLOYMENT_NAME = "gpt-4o"


api_key = os.getenv("AZURE_OPENAI_API_KEY")
api_base = os.getenv("AZURE_OPENAI_API_BASE")
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")


# Initialize the OpenAI Azure client
client = AzureOpenAI(
    api_key=api_key,
    api_version=api_version,
    azure_endpoint=api_base
)

# Create chat completion
response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": " Act as a millionaire and give me the best recommendation that you can"}
    ],
    max_tokens=100,  # Use 'max_tokens' here, Azure-specific
)

# Debug: Print entire response as JSON
print("Full Response:")
print(json.dumps(response.model_dump(), indent=2))

# Safe access and print the AI message content
if response.choices and response.choices[0].message:
    print("\nAI Response:", response.choices[0].message.content)
else:
    print("No response content received.")
