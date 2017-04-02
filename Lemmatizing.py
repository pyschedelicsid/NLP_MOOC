"""Lemmatization usually refers to doing things properly with the use of a vocabulary and morphological analysis of words,
normally aiming to remove inflectional endings only and to return the base or dictionary form of a word, which is known as the lemma."""


from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("call"))
print(lemmatizer.lemmatize("better",pos="a"))
print(lemmatizer.lemmatize("run"))

