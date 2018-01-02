import re

def tokenizer(text):
  lower_text = text.lower()
  return re.findall(r"\w+", lower_text)

def remove_stop_words(stop_words, sentences):
  for word in stop_words:
    if word in sentences:
      sentences.remove(word)
  return sentences
