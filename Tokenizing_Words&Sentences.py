from nltk.tokenize import sent_tokenize, word_tokenize

# tokenizing - word tokenizers.... sentence tokenizers
# lexicon and corporas
# corpora - body of text. ex: medical journals, presidential speeches, English language
# lexicon - words and their meanings

example_text = "Hello Mr. Siddhant, How are you doing today. The weather is great and python is awesome. The sky is pinkish-blue and you should not eat pizza"

print(sent_tokenize(example_text))

print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print i
