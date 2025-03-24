import os
import requests
import json
import csv
from datetime import datetime
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

api_key = os.getenv("AZURE_OPENAI_API_KEY")
api_base = os.getenv("AZURE_OPENAI_API_BASE")
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")

# API endpoint
endpoint = f"{api_base}/openai/deployments/{deployment_name}/chat/completions?api-version={api_version}"

headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}

# User prompt
prompt = "Give me 5 ideas to start with a great content wrting."

payload = {
    "messages": [{"role": "user", "content": prompt}],
    "max_tokens": 100,
    "temperature": 0.7
}

# Capture time
start_time = time.time()

# API request
response = requests.post(endpoint, headers=headers, json=payload)

end_time = time.time()
request_time_ms = int(start_time * 1000)
response_time_ms = int(end_time * 1000)
api_latency_ms = response_time_ms - request_time_ms

# Try parsing response
try:
    response_json = response.json()
    final_response = response_json["choices"][0]["message"]["content"].strip()
except Exception as e:
    response_json = {"error": str(e), "raw_response": response.text}
    final_response = "Error Parsing JSON"

# Print only final response
print(f"Final Response:\n{final_response}")

# Prepare log entry
timestamp = datetime.now().strftime('%Y-%b-%d %H:%M:%S')
log_entry = {
    "timestamp": timestamp,
    "request_time_ms": request_time_ms,
    "response_time_ms": response_time_ms,
    "api_latency_ms": api_latency_ms,
    "response_code": response.status_code,
    "final_response": final_response,
    "prompt": prompt,
    "full_response_json": json.dumps(response_json)
}

# Log file per day
log_date = datetime.now().strftime('%Y-%b-%d')
csv_file = f"openai_logs1_{log_date}.csv"
file_exists = os.path.isfile(csv_file)

# Write to CSV
with open(csv_file, mode='a', newline='', encoding='utf-8') as f:
    fieldnames = log_entry.keys()
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    if not file_exists:
        writer.writeheader()
    writer.writerow(log_entry)