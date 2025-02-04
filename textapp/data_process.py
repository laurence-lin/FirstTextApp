# Define NLP processing tasks
# Candidate tools: SpaCy, Huggingface Transformers, NLTK


from transformers import pipeline


def text_processing(text:str) -> str:
    return text.upper()


def text_summarizing(text: str) -> str:
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)  # Adjust parameters
    return summary[0]['summary_text']