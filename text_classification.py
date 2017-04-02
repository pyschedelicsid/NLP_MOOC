"""To start, we're going to use some sort of binary label. Examples of this could be
identifying text as spam or not, or, like what we'll be doing, positive sentiment or negative sentiment."""

import nltk
import random
from nltk.corpus import movie_reviews

documents = []

for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        documents.append(list(movie_reviews.words(fileid)))

random.shuffle(documents)

#print(documents[1])

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
print(all_words.most_common(15))
print(all_words["stupid"])


