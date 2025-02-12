import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

def generate_text(prompt, model="gemini-pro"):
    response = None

    url = f"https://api.generativeai.google.com/v1beta2/models/{model}:generateText"

    headers = {
        "Authorization" : f"Bearer{API_KEY}",
        "Content_Type" : "application/json"
    }

    data = {
        "prompt" : {
            "text" : prompt
        }
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()

        if response_json and "candidates" in response_json and response_json["candidates"]:
            generated_text = response_json["candidates"][0]["output"]
            return generated_text
        else:
            print("Unexpected Response format: {response_json} ")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error communicating with Gemini API: {e}")
        if response is not None and response.status_code != 200:
            print("Response Status Code :{response.status_code}")
            print("Response content: {response.content}")
        return None

    except (KeyError, IndexError) as e:
        print(f"Error parsing JSON  response as {e} , response : {response_json}")
        return None

    except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None


if  __name__ == "__main__":
    user_prompt = input("enter your prompt:-")
    generated_response = generate_text(user_prompt)

    if generated_response:
        print("Generated Text : - ", generated_response)
    else:
        print("Text Generation Failed")
