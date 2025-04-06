import requests
import json
import fitz  # PyMuPDF

def chat_with_mistral(prompt):
    url = 'http://localhost:11434/api/chat'

    data = {
        "model": "mistral",
        "messages": [
            {"role": "system", "content": "role:\n\n**Position:** Entry-level Fry Cook\n\n**Selection Criteria:**\n- At least 5 years of relevant experience\n- A Bachelor's degree in Health Science\n A CompTIA Culinary+ certification\n\nYour job is to carefully review the resume content and select the single best candidate who meets the most criteria"},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.9,
        "top_p": 0.2,
        "num_predict": 500
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


def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text

# Example usage
fulltext = ""

resume_dict = {
    "marcus_chen": "/data/Marcus Chen.pdf",
    "emily_nguyen": "/data/Emily Nguyen.pdf",
    "diego_martinez": "/data/test2.pdf",
    "alex_johnson": "/data/Alex Johnson.pdf",
    "samantha_lee": "/data/Samantha Lee.pdf"
}

for name in resume_dict:
    text = extract_text_from_pdf(resume_dict[name])
    fulltext += text

chat_with_mistral(fulltext)

