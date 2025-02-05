from django.utils import timezone
from zoneinfo import ZoneInfo

from transformers import pipeline

summarizer = pipeline("summarization")

text = """
Elon Reeve Musk is a businessman and conservative political figure known for his key roles in the automotive company Tesla, Inc. and the space company SpaceX. He is also known for his ownership of the technology company X Corp. and his role in the founding of the Boring Company, xAI, Neuralink, and OpenAI
"""  # Replace with your text


# Summarization
'''
summary = summarizer(text, max_length=150, min_length=30, do_sample=False)  # Adjust parameters
print(summary[0]['summary_text'])
'''

def translate_from_model(text, model_name = 'utrobinmv/t5_translate_en_ru_zh_small_1024', device = 'cpu', translation_order = 'translate to zh: '):
    model = T5ForConditionalGeneration.from_pretrained(model_name) # load model
    model.to(device)
    tokenizer = T5Tokenizer.from_pretrained(model_name) # load model tokenizer

    src_text = translation_order + text

    input_ids = tokenizer(src_text, return_tensors="pt")

    generated_tokens = model.generate(**input_ids.to(device)) # Generate translated result

    result = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True) # Decode translation result

    return result


def translate_long_text(text, chunk_size=500, model_name = 'utrobinmv/t5_translate_en_ru_zh_small_1024', device = 'cpu', translation_order = 'translate to zh: '):  # Adjust chunk_size as needed
    """Translates long text to Chinese by chunking."""
    model = T5ForConditionalGeneration.from_pretrained(model_name) # load model
    model.to(device)
    tokenizer = T5Tokenizer.from_pretrained(model_name) # load model tokenizer

    src_text = translation_order + text
    print("src_text: ", src_text)
    input_ids = tokenizer(src_text, return_tensors="pt").input_ids
    print("input ids: ", input_ids)
    max_len = tokenizer.model_max_length - 2 # Account for start/end tokens with the tokenizer's max length

    translated_chunks = []
    for i in range(0, input_ids.shape[1], max_len):
        print("Working on chunk ", (i+1))
        chunk_input_ids = input_ids[:, i:min(i + max_len, input_ids.shape[1])]
        generated_tokens = model.generate(chunk_input_ids.to(device))
        translated_chunk = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
        translated_chunks.append(translated_chunk)

    return "".join(translated_chunks)  # Combine translated chunks




text = '''
Last week India further slashed import duties on motorcycles, cutting tariffs on heavyweight bikes with engines above 1,600cc from 50% to 30% and smaller ones from 50% to 40%.

A pre-emptive move designed to further smoothen the entry of Harley Davidsons into India - and, Delhi hopes, ward off any threat of tariffs. US motorcycle exports to India were worth $3m last year.

Donald Trump has marked his return to the White House by brandishing trade measures against America's neighbours and allies as well as its big rival China.

India hopes it is ahead of the game - but will its tariff cuts satisfy Trump, or is trade action still on the table?

"Canada and Mexico are literally two arms of the US. If he has acted against them, he could easily act against India too," says Ajay Srivastava, founder of the Delhi-based think tank Global Trade Research Institute (GTRI).

In their phone conversation late last month, the US president pressed Prime Minister Narendra Modi to buy more US arms and for there to be a fairer trade balance, keeping the pressure on.

And during his first term, Trump fixated on India's steep tariffs. He repeatedly slammed the then 100% duty on Harleys as "unacceptable", making it a rallying point in his crusade against what he saw as unfair trade practices.

In the past he repeatedly branded India a "tariff king" and a "big abuser" of trade ties.

India enjoys a trade surplus with the US, its top trading partner. Bilateral trade crossed $190bn (£150bn) in 2023. Merchandise exports to US have surged 40% to $123bn since 2018, while services trade grew 22% to reach $66bn. Meanwhile, US exports to India stood at $70bn.

But beyond bikes, India has zeroed out import taxes on satellite ground installations, benefiting US exporters who supplied $92m worth in 2023.

Tariffs on synthetic flavouring essences dropped from 100% to 20% ($21m in US exports last year), while duties on fish hydrolysate for aquatic feed fell from 15% to 5% ($35m in US exports in 2024). India also scrapped tariffs on select waste and scrap items, a category where US exports amounted to $2.5bn last year.

Top US exports to India in 2023 included crude oil and petroleum products ($14bn), LNG, coal, medical devices, scientific instruments, scrap metals, turbojets, computers and almonds.

"While Trump has criticised India's tariff policies, the latest reductions signal a policy shift that could enhance US exports across various sectors," says Mr Srivastava.

"With key tariff cuts on technology, automobiles, industrial and waste imports, India appears to be taking steps towards facilitating trade even as the global trade environment remains tense."
'''

# Translator
#text = "How old are you?"

print("Length of input text for translation: ", len(text))

from transformers import T5ForConditionalGeneration, T5Tokenizer

result = translate_long_text(text)
print(result)

