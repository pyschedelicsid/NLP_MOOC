"""Named entity recognition is useful to quickly find out what the subjects of discussion are.
NLTK comes packed full of options for us. We can find just about any named entity,
or we can look for specific ones.NLTK can either recognize a general named entity,
or it can even recognize locations, names, monetary amounts, dates, and more."""

import nltk
import numpy
import matplotlib
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)
def process_content():
        try:
            for i in tokenized:
                words = nltk.word_tokenize(i)
                tagged = nltk.pos_tag(words)
                namedEnt = nltk.ne_chunk(tagged)
                namedEnt.draw()

        except Exception as e:
            print(str(e))

process_content()
            






             
                


process_content()


