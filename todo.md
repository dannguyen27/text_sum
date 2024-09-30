Currently using extractive summarization, where sentences are selected directly from the text. While this approach is simpler, it doesn't generate new sentences or paraphrase content.
nlp = spacy.load("en_core_web_sm")


Goal 
Abstractive Summarization: This technique generates new sentences by understanding the text context, rather than selecting sentences directly from the text. It's more complex but can provide more concise and coherent summaries.

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


Alot easier than I though, just had to switch models