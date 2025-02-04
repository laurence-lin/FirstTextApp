from django.utils import timezone
from zoneinfo import ZoneInfo

from transformers import pipeline

summarizer = pipeline("summarization")

text = """
Elon Reeve Musk is a businessman and conservative political figure known for his key roles in the automotive company Tesla, Inc. and the space company SpaceX. He is also known for his ownership of the technology company X Corp. and his role in the founding of the Boring Company, xAI, Neuralink, and OpenAI
"""  # Replace with your text

summary = summarizer(text, max_length=150, min_length=30, do_sample=False)  # Adjust parameters
print(summary[0]['summary_text'])