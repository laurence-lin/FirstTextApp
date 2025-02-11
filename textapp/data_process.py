# Define NLP processing tasks
# Candidate tools: SpaCy, Huggingface Transformers, NLTK

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline


def text_processing(text:str) -> str: # Sample text processing
    return text.upper()


def text_summarizing(text: str) -> str:
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)  # Adjust parameters
    return summary[0]['summary_text']


def text_translate(text, checkpoint = 'facebook/nllb-200-distilled-600M', chunk_size=500, 
                   src_lang = 'eng_Latn', target_lang = 'zho_Hans'): # Adjust chunk_size as needed

    model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    max_input_length = tokenizer.model_max_length - 2 # Account for start/end tokens with the tokenizer's max length
    
    translator = pipeline('translation', model=model, tokenizer=tokenizer, src_lang=src_lang, tgt_lang=target_lang, max_length = 400)
    
    translated_text = ""
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunk_processed = translator(chunk)[0]['translation_text']

        translated_text += chunk_processed
        
    
    return translated_text