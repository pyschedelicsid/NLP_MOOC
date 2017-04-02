"""Part of the NLTK Corpora is WordNet. I wouldn't totally classify WordNet as a Corpora, if anything it is
really a giant Lexicon, but, either way, it is super useful. With WordNet we can do things like look up words
and their meaning according to their parts of speech, we can find synonyms, antonyms, and even
examples of the word in use. """
from nltk.corpus import wordnet

syns = wordnet.synsets("program")
#synset
print(syns[0].lemmas()[0].name)
#just the word
print(syns[0].lemmas()[0].name())

#definition
print(syns[0].definition())

#example
print(syns[0].examples())

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))

#semantic similarity
w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")
print(w1.wup_similarity(w2))



