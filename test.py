import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text

# Example usage
fulltext = ""

resume_dict = {

    "diego_martinez": "/data/test2.pdf",
    "alex_johnson": "/data/Alex Johnson.pdf",
    "marcus_chen": "/data/Marcus Chen.pdf",
    "emily_nguyen": "/data/Emily Nguyen.pdf",
    "samantha_lee": "/data/Samantha Lee.pdf"
}

for name in resume_dict:
    text = extract_text_from_pdf(resume_dict[name])
    fulltext += f"\n=== {name.replace('_', ' ').title()} ===\n"
    fulltext += text

print(fulltext)

