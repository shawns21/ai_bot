import requests
import json

def chat_with_mistral(prompt):
    url = 'http://localhost:11434/api/chat'

    data = {
        "model": "mistral",
        "messages": [
            {"role": "system", "content": "You are an expert recruiter helping evaluate resumes."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.1,
        "top_p": 0.2,
        "num_predict": 50
    }

    response = requests.post(url, json=data, stream=True)  # Enable streaming

    print("Response Generating...")

    full_response = ""
    for line in response.iter_lines():
        if line:
            try:
                parsed = json.loads(line)
                if "message" in parsed and "content" in parsed["message"]:
                    full_response += parsed["message"]["content"]  # Append content
            except json.JSONDecodeError:
                continue  # Ignore invalid lines

    print("\nMistral says:", full_response)
    return full_response

# Example usage
reply = chat_with_mistral("What is the capital of France?")

