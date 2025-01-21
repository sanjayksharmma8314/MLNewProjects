# Load and run the model:

import vllm 
import requests
import resource

#vllm serve "meta-llama/Llama-3.2-11B-Vision-Instruct"

url = "http://localhost:8000/v1/chat/completions"
headers = {"Content-Type": "application/json"}
data = {
    "model": "meta-llama/Llama-3.2-11B-Vision-Instruct",
    "messages": [
        {
            "role": "user",
            "content": "Describe this image in one sentence. Image URL: https://cdn.britannica.com/61/93061-050-99147DCE/Statue-of-Liberty-Island-New-York-Bay.jpg"
        }
    ]
}

# Make the POST request
response = requests.post(url, json=data, headers=headers)

# Print the response
if response.status_code == 200:
    print("Response from server:")
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.text)

