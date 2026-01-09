# backend/nlp.py
# HARD OFFLINE MODE — NO HUGGING FACE, NO INTERNET CALLS

def summarize_text(text):
    if not text:
        return ""
    # Simple fallback summary
    return text[:150] + "..."
