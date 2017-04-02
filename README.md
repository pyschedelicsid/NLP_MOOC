# NLP_MOOC
This repository contains code for an Introductory MOOC on Natural Language Processing MOOC using NLTK. 
NLTK is a leading platform for building Python programs to work with human language data.
It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, 
tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries, and an active discussion forum.

## Setting up the Environment

As I learned this course on Windows. So I'll brief you about how to set up the environment to run the code. 
   First we need to install NLTK using "pip install nltk" in the Command Prompt. Sometimes it may not work out, try to change the path in 
   the environment variable to C:\Python27\Scripts\pip. After this type "import nltk" to check whether base package is installed or not.
   Then type "nltk.download()" A new window should open, showing the NLTK Downloader. Click on the File menu and select Change Download Directory. 
   Test that the data has been installed as follows. (This assumes you downloaded the Brown Corpus):
   >>> from nltk.corpus import brown
   >>> brown.words()
       ['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', ...]
  
 Next we need to install Matplotlib using the command "pip install matplotlib" .
 Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of 
 hardcopy formats and interactive environments across platforms.
 
 Similary we install scikit learn using the "pip install scikit-learn". scikit-learn is an open source Python library that implements a range of 
 machine learning, preprocessing, cross-validation and visualization algorithms using a unified interface.
 
 And lastly install Numpy - "pip install numpy". NumPy is the fundamental package for scientific computing with Python.
 
 Having done all this you're geared up to dive deep into Natural Language Processing using NLTK.
 
