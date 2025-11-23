import json
from docx import Document

def extract_docx_to_json(docx_path: str, json_path: str):
    document = Document(docx_path)

    full_text = "\n".join(p.text for p in document.paragraphs if p.text.strip())

    data = {
        "page": 1,
        "text": full_text,
        "context": "College Students",
        "language": "English",
        "formal": 60,
        "teach": 80,
        "level": "Intermediate",
        "steps": 5,
        "audience": "College CS students"
    }

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Saved JSON to {json_path}")

if __name__ == "__main__":
    extract_docx_to_json("TEST FILE DOCX.docx", "output.json")
