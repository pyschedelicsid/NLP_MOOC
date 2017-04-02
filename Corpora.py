
""" Corpora is just a body of texts. Generally, corpora are grouped by some sort of defining characteristic.
NLTK is a massive toolkit for you. part of what they give you is a ton of highly valuable corpora to learn
with, train against, and some of them are even capable of using in production."""


from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize

sample = gutenberg.raw("bible-kjv.txt")

tok = sent_tokenize(sample)

print(tok[5:15])
